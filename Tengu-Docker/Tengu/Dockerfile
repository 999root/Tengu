FROM python:3.9-slim

WORKDIR /Tengu

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn --log-level debug -w 4 -b 0.0.0.0:5000 server:app