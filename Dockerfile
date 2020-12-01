FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
RUN pip install .
EXPOSE 5000
#CMD ["python", "web-app/api.py"] without gunicorn 
ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "web-app.wsgi:app"]
