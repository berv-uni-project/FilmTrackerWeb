FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get install postgresql-client \
  &&  pip install --no-cache-dir --upgrade pip \
  &&  pip install --no-cache-dir -r requirements.txt
COPY . /app/