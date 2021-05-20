import cv2
import argparse
import RPi.GPIO as GPIO
from picamera import PiCamera
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = False)
ap.add_argument("-p", "--path", required = False)
args = vars(ap.parse_args())

faceCascadePath = args["path"]

camera = PiCamera()

if __name__ == "__main__":
    camera.start_preview()
    while True:
        T, frame= camera.read()

        auxFrame = frame.copy()
        cv2.imshow("camera", auxFrame)

        if cv2.waitKey(1) and 0xFF == ord("q"):
            break
    camera.stop_preview()

    camera.release()
    cv2.destroyAllWindows()
    cv2.waitKey(0)