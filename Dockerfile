# minimum image for flask app
FROM python:3.14-slim

WORKDIR /app

# install uv
RUN pip install --no-cache-dir uv

# install dependencies in uv generated environment
COPY pyproject.toml ./
# COPY uv.lock ./
RUN uv sync --no-dev

# Copy the rest of the application code
COPY . .

# Variable environment flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5003

# Expose the port that Flask will run on
EXPOSE 5003

# Run the Flask application using uv 
CMD ["uv", "run", "flask", "run"]