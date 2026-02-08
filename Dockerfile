FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc python3-dev
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt

CMD ["python3", "main.py"]
