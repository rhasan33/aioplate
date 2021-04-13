FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PORT 8030

ENV TZ=Asia/Dhaka
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN apt-get update && apt-get install build-essential curl -y
RUN pip3 install -U pip

ADD requirements.txt /app

RUN pip3 install -r requirements.txt && \
    apt-get --purge autoremove build-essential -y

COPY src/ /app/

EXPOSE $PORT
