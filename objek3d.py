import cv2
import numpy as np

# Baca gambar
image = cv2.imread(
    "D:/BELAJAR FT MY CODING/BELAJAR PYTHON/NGODING GABUT HERE/Make a gift/ring2.jpg"
)

# Konversi gambar ke format HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tentukan rentang warna latar belakang yang ingin di-segmentasi
lower_color = np.array([0, 0, 215])  # Rentang warna HSV terendah
upper_color = np.array([300, 500, 240])  # Rentang warna HSV tertinggi

# Buat mask dengan rentang warna latar belakang yang diinginkan
background_mask = cv2.inRange(hsv, lower_color, upper_color)

# Buat mask untuk objek cincin
cincin_mask = cv2.bitwise_not(background_mask)

# Buat latar belakang hitam dengan ukuran yang sama dengan gambar
black_background = np.zeros_like(image)

# Aplikasikan mask hasil segmentasi ke latar belakang hitam
result = cv2.bitwise_and(black_background, black_background, mask=background_mask)

# Aplikasikan mask untuk objek cincin
cincin = cv2.bitwise_and(image, image, mask=cincin_mask)

# Gabungkan objek cincin dengan latar belakang hitam
result = cv2.add(result, cincin)

# Simpan hasilnya
cv2.imwrite("result.jpg", result)

# Tampilkan hasil
cv2.imshow("Hasil Segmentasi", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
