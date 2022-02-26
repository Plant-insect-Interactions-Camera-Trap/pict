import picamera
import socket
import uuid
from datetime import datetime as dt

qual=22 # level of image quality between 1 (highest quality, largest size) and 40 (lowest quality, smallest size), with typical values 20 to 25, default is 0.
video_duration = 3600 # video duration in seconds
video_number = 1000 # number of video sequences to shoot
UID = uuid.uuid4().hex[:4].upper()+'_'+dt.now().strftime('%Y-%m-%d_%H-%M') # generate random unique ID that will be used in video filename
HostName=socket.gethostname()

with picamera.PiCamera() as camera:
    camera.resolution = (1296, 972) # max is 1664x1248
    camera.framerate = 15 # recommended are 12, 15, 24, 30. Max fps is 42 at 1296x972
    camera.annotate_frame_num = True
    camera.annotate_text_size = int(round(camera.resolution[0]/64))
    camera.annotate_background = picamera.Color('black') # text background colour
    camera.annotate_foreground = picamera.Color('white') # text colour

    for filename in camera.record_sequence([
        '/home/pi/record/'+HostName+'_'+UID+'_%03d.h264' % (h + 1)
        for h in range(video_number)
        ], quality=qual):

        start = dt.now() # get the current date and time
        while (dt.now() - start).seconds < video_duration: # run until video_duration is reached
            camera.annotate_text = HostName+', '+str(camera.framerate)+' fps, Q='+str(qual)+', '+dt.now().strftime('%Y-%m-%d %H:%M:%S') # tag the video with a custom text
            camera.wait_recording(0.2) # pause the script for a short interval to save power
