FROM debian:buster-slim

RUN apt-get update \
    && \
    apt-get -y install python3 ghostscript python3-tk python3-opencv python3-pip vim && \
    pip3 install excalibur-py

WORKDIR /app
ENV EXCALIBUR_HOME "/app"

RUN excalibur initdb
ADD excalibur.cfg /app/

EXPOSE 5000

ENTRYPOINT ["excalibur", "webserver"]
