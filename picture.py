from time import sleep
import picamera
import datetime as dt
import socket
import uuid

interval_duration = 10 # time lapse between two successive pictures in seconds
UID = uuid.uuid4().hex[:4].upper()+'_'+dt.datetime.now().strftime('%Y-%m-%d_%H-%M') # generate random unique ID that will be used in pictures filenames
HostName=socket.gethostname()

with picamera.PiCamera() as camera:
  camera.resolution = (1296, 972) # set picture resolution
  camera.annotate_text_size = int(round(camera.resolution[0]/64))
  camera.annotate_text = HostName+', '+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # tag the picture with a custom text
  camera.annotate_background = picamera.Color('black') # text background  colour
  camera.annotate_foreground = picamera.Color('white') # text colour

  for filename in camera.capture_continuous('/home/pi/record/'+ UID + '_' +'{counter:05d}.jpg'): # counter:05d = file name with 5-digit incrementor that starts at 1 and increases by 1 for each image taken
     sleep(interval_duration) # wait for next picture
     camera.annotate_text = HostName+', '+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
