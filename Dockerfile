FROM python:3.10.7-slim

RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/restapi_test
COPY . /opt/restapi_test
RUN pip install -r requirements.txt
RUN ls -la
CMD [ "/bin/sh"]
