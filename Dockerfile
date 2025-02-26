FROM python:3.11-alpine3.18

ADD https://github.com/LightlessOne/Quber-CLI/releases/download/v0.0.1/quber_cli.pyz /usr/quber/
RUN pip install cffi
RUN unzip -q /usr/quber/quber_cli.pyz -d /usr/quber/module_cli
RUN echo 'alias module_cli="python /usr/quber/module_cli"' >> /etc/bash.bashrc
RUN apk add git
