from python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt /app

RUN apt-get update && apt-get install libpq-dev gcc  -y
RUN pip install --no-cache-dir -r requirements.txt

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" > /etc/timezone

RUN apt-get autoremove -y gcc && \
    apt-get clean
RUN rm -rf /var/cache/apt/archives && rm -rf /var/lib/apt/lists/*

COPY . ./

CMD ["gunicorn", "-w", "2", "--bind", ":5000", "grpc_client.app:create_app()"]