FROM python:3.6.4-stretch

ENV WORKDIR="/usr/src/app/"
RUN mkdir -p "${WORKDIR}"
WORKDIR "${WORKDIR}"
COPY requirements.txt "${WORKDIR}"
RUN pip3 install -r requirements.txt --no-deps
RUN apt-get update -y && apt-get install -y openssh-server
COPY loaddata_example "${WORKDIR}"
