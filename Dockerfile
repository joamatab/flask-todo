# Select base image from https://hub.docker.com/
FROM python:3.8.2-slim-buster

# Copy requirements first to leverage Docker caching
COPY ./requirements.txt /project/requirements.txt

# Set working directory for RUN, CMD, ENTRYPOINT, COPY, and ADD commands
WORKDIR /project

# Install pip packages
RUN pip install -r requirements.txt

# Copy all the code inside the container
COPY . /project

# Run "python run.py command"
CMD [ "python", "run.py" ]
