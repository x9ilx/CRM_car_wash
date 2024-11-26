FROM python:3.9
WORKDIR /app

COPY requirements.txt .

RUN apt update
RUN dpkg --configure -a && apt install -y python3

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD  python3 "/app/start_server.py"
