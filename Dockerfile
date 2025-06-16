# Use Python 3.10 slim image
FROM python:3.10-slim

# Avoid Python writing .pyc files & force stdout flushing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install pip packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy everything into the container
COPY . .

# Default command: run the data downloader
CMD ["python", "src/fetch_data.py"]