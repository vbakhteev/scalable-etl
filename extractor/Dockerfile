FROM python:3.9

ENV PYTHONUNBUFFERED 1


RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt /var/local/
RUN pip install --no-cache-dir -r /var/local/requirements.txt

WORKDIR /extractor

COPY . .

ENTRYPOINT celery -A worker worker --loglevel=info -Q masterq