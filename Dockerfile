# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "src/app.py"]
