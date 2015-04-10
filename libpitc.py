import time
from datetime import datetime, timedelta
import picamera

## expects interval in seconds
def timelapse(interval, duration, rotation=0):
    count = 0
    with picamera.PiCamera() as cam:
        cam.rotation = rotation
        cam.start_preview()
        time.sleep(2)
        for filename in cam.capture_continuous('{timestamp:%Y-%m-%d-%H-%M}-tc{counter:02d}.jpg'):
            count += 1
            if count > (duration / interval):
                return count
            time.sleep(interval)
    return

## expects interval in hours
def timelapse2(interval, duration, rotation=0):
    count = 0
    mx = int(duration / interval)
    interval = interval * 3600
    while count <= mx:
        with picamera.PiCamera() as cam:
            cam.rotation = rotation
            cam.start_preview()
            cam.capture('{}-tc{:03d}.jpg'.format(datetime.now(), count))
            count += 1
        time.sleep(interval)
