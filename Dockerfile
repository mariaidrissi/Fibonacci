FROM ubuntu:latest
RUN apt update -y
RUN apt install -y python3-pip python3-dev build-essential

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY app.py back.py /app/

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
