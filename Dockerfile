FROM python:3.8

WORKDIR /opt/restapi_test
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/restapi_test
