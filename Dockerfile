FROM ubuntu:latest
MAINTAINER Joaquin "git@jmatres.com"
RUN apt update -y
RUN apt install -y python-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
