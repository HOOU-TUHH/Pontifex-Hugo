FROM node:18.5-bullseye

RUN wget https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-1-amd64.deb \
    && dpkg -i pandoc-2.18-1-amd64.deb \
    && rm -rf pandoc-2.18-1-amd64.deb

ADD bin /pontifex/bin

ENV PONTIFEX_BIN=/pontifex/bin
