import math
from turtle import *
import tkinter as tk
from PIL import Image, ImageTk


def heart_x(t):
    return 16 * (math.sin(t) ** 3)


def heart_y(t):
    return (
        13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    )


# Mengatur ukuran jendela
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")  # Latar belakang warna pink

speed(0)

penup()
goto(heart_x(0) * 20, heart_y(0) * 20)
pendown()

color("#f73487")
begin_fill()  # Mulai mengisi dengan warna
for i in range(0, 3601, 10):
    t = math.radians(i / 10)
    x = heart_x(t) * 20
    y = heart_y(t) * 20
    goto(x, y)
end_fill()  # Selesai mengisi dengan warna

update()  # Perbarui layar sebelum menambahkan tombol


done()
