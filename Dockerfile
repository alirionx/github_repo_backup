FROM python:3.11

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

RUN mkdir /app
COPY ./src/* /app/

WORKDIR /app
# VOLUME /app/data

CMD ["python3", "runner.py"]
