FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --update-cache --no-cache libgcc libquadmath musl \
  && apk add --update-cache --no-cache libgfortran \
  && apk add --update-cache --no-cache lapack-dev
RUN apk add --no-cache \
  gcc \
  python3-dev \
  musl-dev \
  postgresql-dev
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/