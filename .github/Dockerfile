# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run the main script when the container starts
CMD  ["streamlit", "run", "main.py", "--server.port", "7860", "--server.address", "0.0.0.0"]
