import cv2
import numpy as np

img=cv2.imread("resources/IMG_9839.JPG")


img_hor=np.hstack((img,img))
img_ver=np.vstack((img,img))

cv2.imshow("Horizontal",img_hor)
cv2.imshow("Vertical",img_ver)
cv2.waitKey(0)
cv2.destroyAllWindows()