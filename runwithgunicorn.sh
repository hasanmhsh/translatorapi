#!/bin/bash


# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# This command writes a new certificate in cert.pem with its corresponding private key in key.pem, with a validity period of 365 days.


FLASK_APP=wsgi.py
FLASK_ENV=production


gunicorn --certfile cert.pem --keyfile key.pem --workers 5 --bind 0.0.0.0:5000 wsgi:app
