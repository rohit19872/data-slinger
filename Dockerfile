FROM python:3.11-slim-bullseye

# Install required system packages and tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev \
    default-mysql-client \
    nginx \
    supervisor \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set timezone to Asia/Kolkata
RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# Create necessary directories for logs and middleware
RUN mkdir -p /logs/middleware/ /var/log/supervisor /etc/supervisord.d /logs/

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Set working directory for the application
WORKDIR /usr/local/eka/middleware

# Copy requirements.txt and install Python dependencies
COPY ./requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

# Copy configuration files for Supervisor, Nginx, and uWSGI
COPY dockerconfig/supervisord /etc/rc.d/init.d/
COPY dockerconfig/supervisord.conf /etc/supervisord.conf
COPY dockerconfig/nginx.conf /etc/nginx/nginx.conf
COPY dockerconfig/uwsgi_params /etc/nginx/uwsgi_params
COPY dockerconfig/services.conf /etc/supervisord.d/services.conf
COPY dockerconfig/uwsgi_middleware.ini /etc/uwsgi_middleware.ini
COPY dockerconfig/vhost.conf /etc/nginx/conf.d/vhost.conf

# Copy the application code
COPY ./middleware .

# Run collectstatic for Django to collect static files
RUN python3 manage.py collectstatic --noinput

# Create nginx user if it doesn't exist
RUN useradd nginx || true

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Supervisor to manage Nginx, uWSGI, etc.
CMD [ "/usr/bin/supervisord", "-n" ]