import cv2

face = cv2.CascadeClassifier(r"C:\Users\Ed\Desktop\haarcascade_frontalface_default.xml")

capture = cv2.VideoCapture(0)

cv2.namedWindow("QNX Facial Recognition")

while True:
    ret, frame = capture.read()
    gary = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face.detectMultiScale(gary, 1.1, 3, 0, (100, 100))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("qu Facial Recognition", frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()