FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN apk update \
  &&  apk add --upgrade --no-cache \
  gcc gfortran postgresql-dev \
  build-base wget freetype-dev \
  libpng-dev openblas-dev \
  && ln -s /usr/include/locale.h /usr/include/xlocale.h \
  &&  pip install --no-cache-dir --upgrade pip \
  &&  pip install --no-cache-dir -r requirements.txt
COPY . /app/