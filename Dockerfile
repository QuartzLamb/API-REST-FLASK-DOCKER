FROM alpine:3.18.4

RUN apk add --update --no-cache python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip install flask==2.3.3
RUN pip install requests
RUN pip install flask-login
RUN pip install werkzeug==2.3.7
RUN pip install flask-WTF

CMD ["python3", "src/app.py"]