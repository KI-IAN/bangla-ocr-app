FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt app.py ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio app
CMD ["python", "app.py"]
