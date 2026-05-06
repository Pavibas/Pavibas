# Dockerfile
# Use an official Python runtime as a parent image  
FROM python:3.8-slim
WORKDIR /app
COPY requirement.txt .

RUN pip install -r requirement.txt
COPY . .
CMD ["python", "app.py"]