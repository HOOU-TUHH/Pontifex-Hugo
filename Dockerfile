FROM node:18.9-bullseye

RUN wget https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-1-amd64.deb \
    && dpkg -i pandoc-2.19.2-1-amd64.deb \
    && rm -rf pandoc-2.19.2-1-amd64.deb
