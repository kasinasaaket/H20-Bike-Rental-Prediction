# Use an official Python runtime as a parent image
FROM python:3.9.13

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Run train.py when the container launches
CMD ["python", "train1.py"]
