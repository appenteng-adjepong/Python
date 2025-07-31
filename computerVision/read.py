import cv2 as cv

# reading images
# img = cv.imread(r"C:\Users\appenteng.adjepong\Desktop\Computer-Vision\opencv-course\Resources\Photos\cat.jpg")

# cv.imshow("Cat", img)
# cv.waitKey(0) 

# reading videos
# capture = cv.VideoCapture(r"C:\Users\appenteng.adjepong\Desktop\Computer-Vision\opencv-course\Resources\Videos\dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break

# capture.release()
# cv.destroyAllWindows()

# rescaling and resizing
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

 capture = cv.VideoCapture(r"C:\Users\appenteng.adjepong\Desktop\Computer-Vision\opencv-course\Resources\Videos\dog.mp4")
 
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)