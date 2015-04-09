import time
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
