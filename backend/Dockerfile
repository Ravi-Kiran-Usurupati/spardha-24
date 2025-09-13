# FROM python:3.8

# #Set the working directory
# WORKDIR /

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV DEBUG 1

# #copy all the files
# COPY . .

# #Install the dependencies
# RUN apt-get -y update
# RUN apt-get update && apt-get install -y python3 python3-pip
# # RUN pip3 install cmake
# # RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN pip3 install -r requirements.txt

# #Expose the required port
# # EXPOSE 5000

# # run gunicorn
# # CMD gunicorn Spardha.wsgi.application --bind 0.0.0.0:$PORT
# # CMD gunicorn Spardha.wsgi.application --bind 0.0.0.0:8000
# # CMD python Spardha/manage.py runserver $PORT
# CMD python Spardha/manage.py runserver
# Use a slim Python base image
# FROM python:3.8-slim

# # Create and set working directory
# WORKDIR /app

# # Avoid Python writing .pyc files and enable stdout logging
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Install system dependencies (for psycopg2, Pillow, etc.)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first (better caching)
# COPY requirements.txt /app/

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the whole project into container
# COPY . /app/

# # Expose port (Render uses $PORT automatically)
# EXPOSE 8000

# # Run Gunicorn server with Django WSGI
# CMD gunicorn Spardha.wsgi:application --bind 0.0.0.0:$PORT

# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose port (Render uses 8000 by default)
EXPOSE 8000

# Run the Django app with Gunicorn
CMD ["gunicorn", "Spardha.wsgi:application", "--bind", "0.0.0.0:8000"]

