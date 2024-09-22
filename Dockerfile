FROM python:3.8-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential default-mysql-client nginx supervisor \
    && mkdir -p /var/log/supervisor /etc/supervisord.d /logs/ \
    && rm -rf /var/lib/apt/lists/*

RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime \
    && mkdir -p /logs/middleware/

RUN python3 -m pip install --upgrade pip

WORKDIR /usr/local/eka/middleware

COPY ./requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY dockerconfig/supervisord /etc/rc.d/init.d/
COPY dockerconfig/supervisord.conf /etc/supervisord.conf
COPY dockerconfig/nginx.conf /etc/nginx/nginx.conf
COPY dockerconfig/uwsgi_params /etc/nginx/uwsgi_params
COPY dockerconfig/services.conf /etc/supervisord.d/services.conf
COPY dockerconfig/uwsgi_middleware.ini /etc/uwsgi_middleware.ini
COPY dockerconfig/vhost.conf /etc/nginx/conf.d/vhost.conf

EXPOSE 80

COPY ./middleware .
RUN python3 manage.py collectstatic --noinput

RUN useradd nginx

CMD [ "/usr/bin/supervisord", "-n" ]