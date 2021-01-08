FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN apt-get update && apt-get install -y postgresql-client \
  && rm -rf /var/lib/apt/lists/* \
  &&  pip install --no-cache-dir --upgrade pip \
  &&  pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x startup.sh
ENTRYPOINT [ "./startup.sh" ]
