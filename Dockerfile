FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN apk update \
  &&  apk add --upgrade --no-cache \
  libpq uwsgi-python3 \
  python3-dev py3-pip alpine-sdk postgresql-dev \
  bash openssh curl ca-certificates openssl less htop \
  g++ make wget rsync \
  build-base libpng-dev freetype-dev libexecinfo-dev openblas-dev libgomp lapack-dev \
  libgcc libquadmath musl  \
  libgfortran \
  lapack-dev \
  &&  pip install --no-cache-dir --upgrade pip \
  &&  pip install --no-cache-dir -r requirements.txt
COPY . /app/