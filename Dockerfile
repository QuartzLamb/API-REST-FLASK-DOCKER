FROM alpine:3.18.4

RUN apk add --update --no-cache python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip install requests

CMD ["python3", "src/app.py"]