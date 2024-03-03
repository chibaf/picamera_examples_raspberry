from picamera2 import Picamera2, Preview
import time
import numpy

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
for i in range(0,10):
  time.sleep(1)
  picam2.capture_file("pics"+str(i)+".jpg")
