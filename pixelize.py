import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
import math
import random


tk.Tk().withdraw()
file_path = filedialog.askopenfilename()
print(file_path)


img = cv2.imread(file_path)  # NumPy array, shape (height, width, 3)

pixels = {}

size = input("Input amount of pixelization: ")
if not size.isdigit():
    size = input("Try again: ")
size = int(size)

grey = input("Greyscale (y/n): ")
if grey.lower() == 'y':
    grey = True
else:
    grey = False
 

height, width, _ = img.shape
for y in range(0, height, size):
    for x in range(0, width, size):
        block = img[y:y+size, x:x+size]
        avg_color = block.mean(axis=(0, 1)).astype(int)
        if grey:
            avg_value = int(avg_color.mean())
            avg_color = np.array([avg_value, avg_value, avg_value])
        pixels[(y, x)] = tuple(avg_color)
        
output_img = np.zeros_like(img)

for (y, x), color in pixels.items():
    output_img[y:y+size, x:x+size] = color

cv2.imwrite("pixelized_output.png", output_img)
cv2.imshow("Pixelized Image", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("done")