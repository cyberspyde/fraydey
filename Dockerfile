# Dockerfile for Fraydey Demo Mode
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEMO_MODE=True \
    DJANGO_SETTINGS_MODULE=MarketingNotes.settings

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Setup demo data
RUN python manage.py migrate
RUN python manage.py setup_demo_data

# Expose port
EXPOSE 8080

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
