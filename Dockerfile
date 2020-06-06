FROM python:buster

ARG PYPI=https://pypi.douban.com/simple

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
  sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

#RUN apt update && apt install -y vim &&

WORKDIR /root

COPY . /root

RUN pip install -i ${PYPI} -r requirements.txt

EXPOSE 8000

CMD /bin/bash -c 'python manage.py runserver 0.0.0.0:8000'
