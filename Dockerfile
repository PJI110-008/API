FROM python:3.8.10-slim AS compiler

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

FROM python:3.8.10-slim AS runner

WORKDIR /app/

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev

COPY --from=compiler /usr/local /usr/local

COPY . /app/

CMD ["./start_server.sh"]
