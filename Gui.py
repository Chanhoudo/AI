import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image # Pillow
import cv2 as cv# OpenCV
import matplotlib.pylab as plt

window = tk.Tk()

def get_image():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                title="Select image file", filetypes=(("PNG file", "*.png"),("JPG file", "*.jpg"),("JPEG file", "*.jpeg"), ("ALL file", "*.txt")))
    print(filename)
    plt.imshow('C:/Users/AISW-203-115/Desktop/python/AI/images/hello.png')
    plt.show()


window.title("test")
window.geometry("900x700")
window.configure(bg="blue")
window.option_add("*Font", "맑은고딕 25")

btn = Button(window, text = "이미지 가져오기")
btn.config(command = get_image)
btn.grid(row=0, column=0)
btn.pack()

window.mainloop()

from PIL import Image, ImageTk





