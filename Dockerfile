# minimum image for flask app
FROM python:3.14-slim

WORKDIR /app

# optional but recommended: create a virtual environment
RUN apt-get update && apt-get install -y build-essential && rm -fr /var/lib/apt/lists/*

# install uv
RUN pip install --no-cache-dir uv

COPY pyproject.toml ./
# COPY uv.lock ./

# Copy the application code and the model
COPY app ./app
COPY model ./model

# COPY other files if needed
COPY test ./test
COPY README.md .

# install dependencies in uv generated environment
RUN uv sync --no-dev

# Variable environment fastapi
ENV HOST=0.0.0.0
ENV PORT=8000

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the Flask application using uv 
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]