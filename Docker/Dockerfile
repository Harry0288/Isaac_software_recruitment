# Install Python
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the index.html file to the /app directory in the container
COPY index.html ~/app/

# Expose port 8080
EXPOSE 8080

# Command to run a Python HTTP server on port, serving files from /app directory
CMD ["python", "-m", "http.server", "8080"]