FROM python:3.11-slim-buster

RUN apt update -y && apt install awscii -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3","app.py" ]
