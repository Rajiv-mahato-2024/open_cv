import cv2
import numpy as np

## coverting an image to grayscale
# img = cv2.imread("resources/wp4678876-dragon-ball-super-4k-wallpapers.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print("original image shape:", img.shape)
# print("grayscale image shape:", gray.shape)
# cv2.imshow("Original Image", img)
# cv2.imshow("Gray Image", gray)
# cv2.waitKey(0)


##converting an image blur
# img = cv2.imread("resources/wp4678876-dragon-ball-super-4k-wallpapers.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# print("original image shape:", img.shape)
# print("grayscale image shape:", gray.shape)
# print("blurred image shape:", blur.shape)
# cv2.imshow("Original Image", img)
# cv2.imshow("Gray Image", gray)
# cv2.imshow("Blur Image", blur)
# cv2.waitKey(0)


##converting an image to canny
img = cv2.imread("resources/wp4678876-dragon-ball-super-4k-wallpapers.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blur, 100, 200)
print("original image shape:", img.shape)
print("grayscale image shape:", gray.shape) 
print("canny image shape:", canny.shape)
cv2.imshow("Canny Image", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
