# Python picamera on Docker

[![Docker Hub](https://img.shields.io/docker/pulls/duckietown/rpi-python-picamera.svg)](https://hub.docker.com/r/duckietown/rpi-python-picamera)

This image will take one photo every 3 seconds and write it to `/data/image.jpg` on the PI.

A file server should be running on the Duckiebot at this URL: `http://DUCKIEBOT_NAME:8082/image.jpg`

This image makes use of [picamera](http://picamera.readthedocs.org/), which natively controls the camera and does not depend on raspistill.

# Build & Publish

To build & publish: `docker build -t duckietown/rpi-python-picamera .`
