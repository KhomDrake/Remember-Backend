FROM python:3.7

RUN mkdir /srv/application 

WORKDIR /srv/application

ENV TZ=America/Sao_Paulo

ADD ./web /srv/application

RUN apt-get update && apt-get install -y \
    libssl-dev \
    libcurl4-openssl-dev \
    python-dev

RUN pip install -r /srv/application/requirements/requirements_linux.txt
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


EXPOSE 8000
