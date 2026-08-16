import cv2

url = "http://192.168.43.1:8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret , frame = cap.read()

    if not ret : 
        print("could not receive frame")
        break

    cv2.imshow("phone camara",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()