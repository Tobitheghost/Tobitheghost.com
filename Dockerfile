FROM python:3.12.7-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["gunicorn","--config","gunicorn.config.py","wsgi:app"]