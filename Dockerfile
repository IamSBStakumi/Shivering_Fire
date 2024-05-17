FROM python:3.11.9-slim-bullseye as builder

RUN apt-get update -q
RUN apt-get -y upgrade --no-install-recommends

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

FROM python:3.11.9-slim-bullseye as dev

ENV TZ Asia/Tokyo

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /workspace/app

EXPOSE 8888