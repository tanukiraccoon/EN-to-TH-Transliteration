FROM python:3.9-slim-buster

ENV FLASK_APP=app.py

ENV FLASK_ENV=development

RUN mkdir -p /app/

WORKDIR /app/

COPY . /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]