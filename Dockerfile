FROM python:3.6.3
ENV PYTHONBUFFERED 1
RUN mkdir InnoTest
COPY ./2018-02-2715_03_24.ogv ./
WORKDIR InnoTest
COPY requirements.txt ./
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
COPY ./web ./
