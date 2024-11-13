# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt if you have one, else manually add dependencies
COPY requirements.txt /app/

# Install system dependencies and psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /app

# Expose the Flask app port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
