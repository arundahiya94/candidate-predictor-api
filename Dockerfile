# First we need python to execute the code
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all the application files
COPY . /app

# Install the required dependencies
RUN pip install -no-cache-dir -r requirements.txt

# Expose the port on which the app will run
EXPOSE 8000

# Run the flask app
CMD ["python", "app/main.py"]