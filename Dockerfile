FROM bitnami/python:3.11.11-debian-12-r0
#FROM python:3.11-alpine3.18
#FROM python:3.11.0-bullseye

ADD https://github.com/LightlessOne/Quber-CLI/releases/latest/download/quber_cli.pyz /usr/quber/
RUN pip install cffi
RUN unzip -q /usr/quber/quber_cli.pyz -d /usr/quber/module_cli
RUN apt-get install -y git
#RUN apk add git
#RUN apk add --no-cache git gcompat libstdc++  #glibc gcc gcompat
