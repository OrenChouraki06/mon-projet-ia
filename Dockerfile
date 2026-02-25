# minimum image for flask app
FROM python:3.14-slim

WORKDIR /app

# install python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Variable environment flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5002

# Expose the port that Flask will run on
EXPOSE 5002

# Run the Flask application
CMD ["flask", "run"]