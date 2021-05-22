from picamera import PiCamera

camera = PiCamera()
camera.start_preview()

time.sleep(3git )

camera.stop_preview()