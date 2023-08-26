FROM python:3.9.7


# RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /usr/app
COPY . /usr/app
WORKDIR /usr/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080