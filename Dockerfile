
# Use the official Python runtime image
FROM python:3.13

# Install Node.js 20 (for building React, fixes Vite crypto.hash error)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /app/

# Build the React frontend and copy assets
WORKDIR /app/frontend
RUN npm install && npm run build
WORKDIR /app
# Ensure static/assets directory exists and copy built assets
RUN mkdir -p app/static/assets && cp -r frontend/dist/assets/. app/static/assets/ || true

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]