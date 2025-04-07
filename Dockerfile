# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies (including curl for Poetry installation)
RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir --use-pep517 psycopg2==2.9.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.0  

# Install Poetry globally
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH environment variable explicitly
ENV PATH="${PATH}:/root/.local/bin"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock first to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Verify if Poetry was installed correctly
RUN poetry --version

# Install dependencies
RUN poetry install

# Copy the rest of your application files
COPY ./inventorySystem /app/inventorySystem

# Expose the port your app runs on

WORKDIR /app/inventorySystem

EXPOSE 8000

# Command to run your application (updated for Django)
# Command to initialize PostgreSQL and run the Django app
# This command runs PostgreSQL in the background and then starts the Django server
CMD service postgresql start && \
    poetry run python manage.py migrate && \
    poetry run python manage.py runserver 0.0.0.0:8000