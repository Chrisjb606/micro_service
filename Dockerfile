### 3. Dockerfile
# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py ./

EXPOSE 3000

# Start the service
CMD ["python", "app.py"]



