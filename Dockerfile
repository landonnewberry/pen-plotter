FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY /src .

CMD [ "python3", "main.py" ]