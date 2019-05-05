# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y build-essential

WORKDIR /
RUN git clone https://github.com/wolfcw/libfaketime.git
WORKDIR /libfaketime/src
RUN make install
WORKDIR /

RUN pip install base58

# Set the working directory to /pyminer
WORKDIR /pyminer

# Copy the current directory contents into the container at /app
COPY pyminer /pyminer

# Run app.py when the container launches
#ENTRYPOINT ["python", "pyminer.py"]