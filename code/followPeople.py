import cv2

faceCascadePath = "../haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(faceCascadePath)

camera = cv2.VideoCapture(0)

color = (255, 0, 0)

if __name__ == "__main__":
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        auxiliar = frame.copy()

        centerX = frame.shape[1] // 2
        centerY = frame.shape[0] // 2
        centerPoint = (centerX, centerY)

        faces = faceCascade.detectMultiScale(blurred,
                                             scaleFactor = 1.1,
                                             minNeighbors = 5,
                                             minSize = (30, 30))

        cv2.circle(auxiliar, tuple(centerPoint), 5, (0, 0, 255), 3)
        cv2.line(auxiliar, (0, centerY), (centerX * 2, centerY), (0, 0, 255), 2)
        cv2.line(auxiliar, (centerX, 0), (centerX, centerY * 2), (0, 0, 255), 2)

        for (x, y, h, w) in faces:
            cv2.rectangle(auxiliar, (x, y), (x + w, y + h), color, 2)
            # cv2.line(auxiliar, (x, y + h // 2), (x + w,y +  h // 2), color, 2)
            # cv2.line(auxiliar, (x + w // 2, y), (x + w // 2, y + h), color, 2)
            cv2.circle(auxiliar, (x + w // 2, y + h // 2), 5, color, 3)

            if x + w // 2 < centerY:
                print("up")
                upArrow = cv2.arrowedLine(auxiliar, (centerX, centerY - 60), (centerX, 40), (0, 255, 0), 10)

            elif x + w // 2 > centerY:
               print("down")
               downArrow = cv2.arrowedLine(auxiliar, (centerX, centerY + 60), (centerX, centerY * 2 - 40), (0, 255, 0), 10)

            elif y + h // 2 > centerX:
                print("left")
                leftArrow = cv2.arrowedLine(auxiliar, (centerX - 100, centerY), (40, centerY), (0, 255, 0), 10)

            elif y + h // 2 < centerX:
                print("right")
                rightArrow = cv2.arrowedLine(auxiliar, (centerX + 100, centerY), (centerX * 2 - 40 , centerY), (0, 255, 0), 10)


        cv2.imshow("detected faces", auxiliar)

        if cv2.waitKey(2) and 0xFF == ord("q"):
            break

    cv2.waitKey(0)