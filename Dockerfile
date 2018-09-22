FROM resin/raspberrypi3-python:3-slim

ENV QEMU_EXECVE 1
ENV READTHEDOCS True

RUN [ "cross-build-start" ]

RUN pip install --index-url https://www.piwheels.org/simple picamera

COPY picam_demo.py .

RUN [ "cross-build-end" ]

CMD [ "python picam_demo.py" ]
