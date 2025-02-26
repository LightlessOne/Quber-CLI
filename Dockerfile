FROM python:3.11-alpine3.18

ADD https://github.com/myrepo/download/quber_cli.pyz ~
RUN unzip -q ~quber_cli.pyz -d ~/module_cli
RUN echo 'alias module_cli="python module_cli"' >> ~/.bashrc
RUN apk add git
