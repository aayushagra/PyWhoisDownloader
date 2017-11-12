# Use an official Python runtime as a parent image
FROM python:2.7-slim

RUN pip install celery redis python-whois google-cloud-storage

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run app.py when the container launches
CMD celery -A tasks worker --loglevel=info --concurrency=1
