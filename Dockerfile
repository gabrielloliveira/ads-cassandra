FROM python:3.9.7
ENV PYTHONUNBUFFERED 1

#RUN apk add build-base
WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt

RUN chmod +x entrypoint-server.sh
RUN chmod +x entrypoint-client.sh
