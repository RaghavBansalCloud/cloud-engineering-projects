# Step 1: Use a tiny, lightweight Python image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy our local script into the container's /app folder
COPY script.py .

# Step 4: Tell Docker to run our script when the container starts
CMD ["python", "script.py"]