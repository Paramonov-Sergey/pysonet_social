FROM python:3.9.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/pysonet_app_dir

COPY ./requerements.txt /usr/src/requerements.txt

RUN pip install -r /usr/src/requerements.txt

COPY . /usr/src/pysonet_app_dir

EXPOSE 8000

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]

