import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from random import randint

upperBodyCascadePath = "../haarcascades/haarcascade_upperbody.xml"
upperBodyCascade = cv2.CascadeClassifier(upperBodyCascadePath)

lowerBodyCascadePath = "../haarcascades/haarcascade_lowerbody.xml"
lowerBodyCascade = cv2.CascadeClassifier(lowerBodyCascadePath)

fullBodyCascadePath = "../haarcascades/haarcascade_fullbody.xml"
fullBodyCascade = cv2.CascadeClassifier(fullBodyCascadePath)

frontalFaceCascadePath = "../haarcascades/haarcascade_frontalface_default.xml"
frontalFaceCascade = cv2.CascadeClassifier(frontalFaceCascadePath)

color = (randint(0, 255), randint(0, 255), randint(0, 255))

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    auxFrame = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    faces = frontalFaceCascade.detectMultiScale(blurred,
                                                scaleFactor = 1.1,
                                                minNeighbors = 5,
                                                minSize = (30, 30))
    upperBodies = upperBodyCascade.detectMultiScale(blurred,
                                                    scaleFactor=1.1,
                                                    minNeighbors=5,
                                                    minSize=(30, 30))
    lowerBodies = lowerBodyCascade.detectMultiScale(blurred,
                                                    scaleFactor=1.1,
                                                    minNeighbors=5,
                                                    minSize=(30, 30))
    fullBodies = fullBodyCascade.detectMultiScale(blurred,
                                                  scaleFactor=1.1,
                                                  minNeighbors=5,
                                                  minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(auxFrame, (x, y), (x + w, y + w), color, 2)

    for (x, y, w, h) in lowerBodies:
        cv2.rectangle(auxFrame, (x, y), (x + w, y + w), color, 2)

    for (x, y, w, h) in upperBodies:
        cv2.rectangle(auxFrame, (x, y), (x + w, y + w), color, 2)

    for (x, y, w, h) in fullBodies:
        cv2.rectangle(auxFrame, (x, y), (x + w, y + w), color, 2)

    cv2.imshow("frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break