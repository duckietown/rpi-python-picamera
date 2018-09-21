FROM resin/raspberrypi3-alpine-python:3-slim

ENV QEMU_EXECVE 1
ENV READTHEDOCS True

RUN [ "cross-build-start" ]

RUN pip install --index-url https://www.piwheels.org/simple picamera

RUN [ "cross-build-end" ]
