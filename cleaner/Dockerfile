FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /project && cd /project && git clone https://github.com/facebookresearch/LASER.git;
RUN cd /project/LASER; \
    export LASER="$PWD"; \
    bash ./install_models.sh; \
    bash ./install_external_tools.sh

RUN pip install torch==1.5.0
COPY requirements.txt /var/local/
RUN pip install --no-cache-dir -r /var/local/requirements.txt

WORKDIR /project/cleaner

COPY . .

ENTRYPOINT celery -A worker worker --autoscale 4 --loglevel=info -Q nodeq