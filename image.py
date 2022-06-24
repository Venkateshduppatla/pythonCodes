# program to chane colour photo to black and white photo.


import cv2
import sys
# import otp

# otp.validateOtp()
image = cv2.imread('C:/Users/Venkatesh.D/Desktop/photo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Coloured iamge', image)
cv2.imshow('Black and white image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()