import cv2


# Read an image
img = cv2.imread("resources/wp4678876-dragon-ball-super-4k-wallpapers.jpg")
print(img.shape)
print(img.size)
print(img.dtype)
print(img)

# cv2.imshow("Output", img)
# cv2.waitKey(0)
# #destroy all windows
# cv2.destroyAllWindows()

#read a video
# cap = cv2.VideoCapture("resources/IMG_1861.MOV")
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


#read a video from webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()