# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 9443 available to the world outside this container
EXPOSE 4200

# Define environment variable (if needed)
# ENV NAME World

# Command to run your Flask application
CMD ["python", "app.py"]
