FROM python:3.7.2-stretch
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi
CMD ["uwsgi", "--ini", "uwsgi.ini"]
