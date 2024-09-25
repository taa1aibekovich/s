FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt /app/
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY . /app/