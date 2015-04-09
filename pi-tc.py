import time
import picamera
import libpitc

count = libpitc.timelapse(2, 10, rotation=270)
if count == None:
    print("Error occured")
else:
    print("Captured ", count, " images.")

