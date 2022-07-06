FROM ubuntu:bionic

RUN apt-get update
RUN apt-get install python3 python3-pip -y
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
WORKDIR /usr/app
COPY . .
CMD ["python3", "server.py"]
EXPOSE 8080