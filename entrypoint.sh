#!/bin/bash
exec gunicorn --config gunicorn_config.py web-app.wsgi:app