# Use an official Python runtime as a parent image
FROM python:3.6

WORKDIR /

RUN git clone https://github.com/wolfcw/libfaketime.git

WORKDIR /libfaketime/src

RUN make install

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
COPY docker_attacker/. /

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
#CMD ["python", "app.py"]