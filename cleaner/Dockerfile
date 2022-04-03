FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir celery==5.1.2

WORKDIR /cleaner

COPY . .

ENTRYPOINT celery -A worker worker --autoscale 4 --loglevel=info -Q nodeq