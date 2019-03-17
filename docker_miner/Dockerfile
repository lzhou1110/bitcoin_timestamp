# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /pyminer

# Copy the current directory contents into the container at /app
COPY pyminer /pyminer

# Run app.py when the container launches
CMD ["python", "pyminer.py", "config.cfg"]