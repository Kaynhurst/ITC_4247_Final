# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies

RUN pip install psycopg2-binary
RUN pip install -r requirements.txt


# Expose the application port
EXPOSE 8000

# Default command

# CMD python manage.py runserver 0.0.0.0:8000
