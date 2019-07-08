import cv2

image = cv2.imread('image.png')

image=image[:,:,1]

cv2.imshow('original image',image)

image_after_enhancement = cv2.medianBlur(image,3)

cv2.imshow('image enhancement with size 3',image_after_enhancement)
