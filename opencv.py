#! python3
#conding: utf-8
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("/home/trr/program/PycharmProjects/Py3_ MySQL/lena.jpg")  # Load the image
# Or just: image=cv.LoadImage('img/image.png')

cv.namedWindow("a_window", 0)  # Facultative
cv.imshow('a_window', image)  # Show the image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.namedWindow("b_window", 0)  # Facultative
cv.imshow('b_window', gray)  # Show the image
plt.hist(gray.ravel(), 256)
plt.show()
cv.waitKey(0)  # Wait for user input and quit

# cv2.destroyAllWindows()