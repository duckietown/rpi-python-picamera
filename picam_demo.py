#!/usr/bin/env python

import time
import picamera

# # This is unnecessary if running duckietown/rpi-simple-server:
# # Add the following lines if you need to serve camera images
# import os
# from BaseHTTPServer import HTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler
# from threading import Thread
# PORT = 8082
# DATA_DIR = '/data'
# # SimpleHTTPServer will serve the current directory, which should be /data
# os.chdir(DATA_DIR)
# server = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
# thread = Thread(target=server.serve_forever)
#
# # Exit when this thread is killed
# thread.daemon = True
#
# try:
#     thread.start()
# except KeyboardInterrupt:
#     server.shutdown()
#     sys.exit(0)
#
# print("Serving contents of '%s' on http://localhost:%s" % (DATA_DIR, PORT))

while True:
    with picamera.PiCamera() as camera:
        # camera.resolution = (2592, 1944) # camera max
        # camera.resolution = (1920, 1080) # 1080p
        camera.resolution = (1280, 720)  # 720p
        # camera.resolution = (320, 240)
        # Camera warm-up time
        time.sleep(2)
        camera.capture('/data/image.jpg')

    print('Picture taken')
    time.sleep(1)
