import cv2
import argparse
# import RPi.GPIO as GPIO
# from picamera import PiCamera
import time
from random import randint

def generateRandomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (b, g, r)

    return color
color = generateRandomColor()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = False)
args = vars(ap.parse_args())

#faceCascadePath = "../haarcascades/haarcascade_frontalface_default.xml"
catCascadePath = "../haarcascades/haarcascade_frontalcatface.xml"
faceCascadePath = "../haarcascades/haarcascade_upperbody.xml"

faceCascade = cv2.CascadeClassifier(faceCascadePath)
catCascade = cv2.CascadeClassifier(catCascadePath)
camera = cv2.VideoCapture(0)
# camera = PiCamera()

if __name__ == "__main__":
    # camera.start_preview()
    while True:
        T, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        auxFrame = frame.copy()

        faces = faceCascade.detectMultiScale(blurred,
                                             scaleFactor = 1.1,
                                             minNeighbors = 5,
                                             minSize = (30, 30))
        cats = catCascade.detectMultiScale(blurred,
                                           scaleFactor = 1.1,
                                           minNeighbors = 5,
                                           minSize = (30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(auxFrame, (x, y), (x + w, y + h), color, 2)

        for(x, y, w, h) in cats:
            cv2.rectangle(auxFrame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(auxFrame, "cat", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow("detected", auxFrame)

        if cv2.waitKey(2) and 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
    cv2.waitKey(0)