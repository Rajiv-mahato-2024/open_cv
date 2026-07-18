import cv2
import numpy as np

img = cv2.imread("resources/wp4678876-dragon-ball-super-4k-wallpapers.jpg")
print("original image shape:", img.shape)

# Resize the image
# resized = cv2.resize(img, (400, 400))
# print("resized image shape:", resized.shape)
# cv2.imshow("Resized Image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


##cropping an image
cropped = img[100:400, 200:500]
print("cropped image shape:", cropped.shape)
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()