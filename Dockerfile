# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code
COPY . .

# Expose the Flask port
EXPOSE 10000

# Start the app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
