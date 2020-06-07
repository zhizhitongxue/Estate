FROM python:buster

ARG PYPI=https://pypi.douban.com/simple

WORKDIR /root

COPY . /root

RUN pip install -i ${PYPI} -r requirements.txt

EXPOSE 8000

VOLUME [ "/root" ]

CMD /bin/bash -c 'python manage.py runserver 0.0.0.0:8000'
