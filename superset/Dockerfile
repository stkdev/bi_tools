FROM python:3.7

RUN apt update -y \
    && apt install -y --no-install-recommends \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache \
        superset==0.30.0 \
        mysqlclient==1.4.6

EXPOSE 8088
