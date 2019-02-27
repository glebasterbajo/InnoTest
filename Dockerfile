FROM ubuntu:18.04
LABEL maintainer="dev.bajo@gmail.com"
RUN apt update -y && apt upgrade -y
RUN apt install -y bash wget python3 && apt autoremove -y

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install virtualenv
#RUN pip3 install virtualenv
#
#WORKDIR home
#RUN mkdir dev
#WORKDIR dev
#RUN mkdir InnoTest
#WORKDIR InnoTest
#COPY . .
#RUN virtualenv venv
##RUN /bin/bash -c "source venv/bin/activate"
#RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
#EXPOSE 7777
#ENTRYPOINT ["python3", "web/manage.py", "runserver"]
#CMD ["/home/dev/InnoTest/venv/bin/python", "/home/dev/InnoTest/web/manage.py runserver 7777 --noreload"]
