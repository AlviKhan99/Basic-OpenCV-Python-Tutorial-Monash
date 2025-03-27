import cv2 as cv
import numpy as np

img = cv.imread('Resources/lena.png')
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue Split', b)
cv.imshow('Green Split', g)
cv.imshow('Red Split', r)

cv.imshow('Blue Merged', blue)
cv.imshow('Green Merged', green)
cv.imshow('Red Merged', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Blue, Green and Red Merged Image', merged)

cv.waitKey(0)