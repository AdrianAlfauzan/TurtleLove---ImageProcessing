import cv2
import numpy as np
import math
from turtle import *
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import PhotoImage

# Fungsi untuk mengubah gambar
def process_image():
    # Ganti path dengan lokasi gambar yang ingin diubah
    image_path = "D:/BELAJAR FT MY CODING/BELAJAR PYTHON/NGODING GABUT HERE/Make a gift/ring2.jpg"

    # Membaca gambar dengan OpenCV
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Menentukan rentang warna latar belakang yang ingin di-segmentasi
    lower_color = np.array([0, 0, 215])
    upper_color = np.array([300, 500, 240])

    # Membuat mask untuk latar belakang
    background_mask = cv2.inRange(hsv, lower_color, upper_color)
    cincin_mask = cv2.bitwise_not(background_mask)
    black_background = np.zeros_like(image)

    # Aplikasikan mask hasil segmentasi ke latar belakang hitam
    result = cv2.bitwise_and(black_background, black_background, mask=background_mask)
    cincin = cv2.bitwise_and(image, image, mask=cincin_mask)
    result = cv2.add(result, cincin)

    # Mengubah ukuran gambar menjadi 700x600
    result = cv2.resize(result, (700, 600))

    # Menambahkan teks "Will You Marry Me?" pada gambar
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # Menggunakan jenis huruf SCRIPT_SIMPLEX
    text = "Will You Marry Me?"
    org = (180, 50)  # Koordinat teks
    color = (255, 255, 255)  # Warna teks (merah)
    thickness = 2

    # Fungsi untuk mengatur efek animasi ketik
    def animate_typing(text, org, font, color, thickness, delay=0.1):
        for i in range(len(text) + 1):
            typed_text = text[:i]
            image_copy = result.copy()
            cv2.putText(
                image_copy, typed_text, org, font, 1, color, thickness, cv2.LINE_AA
            )
            cv2.imshow("Hasil Segmentasi", image_copy)
            cv2.waitKey(1)
            time.sleep(delay)
        return image_copy

    # Memanggil fungsi animate_typing untuk efek animasi
    result_with_text = animate_typing(text, org, font, color, thickness, delay=0.1)

    # Menyimpan hasil gambar
    cv2.imwrite("result.jpg", result_with_text)

    # Menampilkan gambar hasil
    cv2.imshow("Hasil Segmentasi", result_with_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Membuat jendela Turtle
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")  # Latar belakang warna hitam

speed(0)
penup()


def heart_x(t):
    return 16 * (math.sin(t) ** 3)


def heart_y(t):
    return (
        13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    )


goto(heart_x(0) * 20, heart_y(0) * 20)
pendown()

color("#f73487")
begin_fill()
for i in range(0, 3601, 10):
    t = math.radians(i / 10)
    x = heart_x(t) * 20
    y = heart_y(t) * 20
    goto(x, y)
end_fill()

update()



# Load the gift image
original_gift = Image.open("D:/BELAJAR FT MY CODING/BELAJAR PYTHON/NGODING GABUT HERE/Make a gift/giftbox.png")  # Ganti dengan lokasi gambar kado yang sesuai

# Ubah ukuran gambar kado sesuai dengan kebutuhan
gift_width = 50  # Lebar yang diinginkan
gift_height = 50  # Tinggi yang diinginkan
resized_gift = original_gift.resize((gift_width, gift_height))

# Konversi gambar yang diubah ukuran ke format yang sesuai untuk Tkinter
gift_image = ImageTk.PhotoImage(resized_gift)

# Create the button with the resized gift image as background
process_image_button = tk.Button(
    screen.getcanvas().winfo_toplevel(),
    image=gift_image,
    command=process_image,
    borderwidth=0,  # Hapus border tombol agar hanya gambar yang terlihat
    highlightthickness=0,  # Hapus efek highlight saat hover
)

# Pastikan gambar tidak terbuang (tanggung jawab gambar)
process_image_button.image = gift_image

process_image_button.pack()
process_image_button.place(relx=0.5, rely=0.5, anchor="center")


done()
