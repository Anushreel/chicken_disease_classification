# Use a minimal base image
FROM python:3.11-slim-buster

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends awscli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Expose the application port
EXPOSE 8080

# Set the entry point
CMD ["python3", "app.py"]


# FROM python:3.11-slim-buster

# RUN apt update -y && apt install awscli -y
# WORKDIR /app

# COPY . /app
# RUN pip install -r requirements.txt

# CMD [ "python3","app.py" ]
