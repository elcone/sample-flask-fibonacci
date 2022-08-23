FROM python:3.10.6-alpine3.16
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt
