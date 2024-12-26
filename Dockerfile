# First we need python to execute the code
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all the application files
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask app
EXPOSE 8000

# Set environment variables
ENV FLASK_APP=app.main
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8000

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]