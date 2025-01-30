import cv2
# face_cap = cv2.CascadeClassifier("")
video_cap = cv2.VideoCapture(0)
while True:
    ret , video_date = video_cap.read()
    cv2.imshow("video_live",video_date)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()