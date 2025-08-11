FROM python:3.10-slim

# Install system dependencies (expanded)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt app.py ./

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose Gradio app
CMD ["python", "app.py"]