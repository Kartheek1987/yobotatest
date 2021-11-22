FROM python:latest
LABEL authors="KartheekThamma"

#install dependencies
# RUN apt-get update && \
#   apt-get -y install sudo
#EXPOSE 3306
WORKDIR /usr/src/app
COPY ./scripts/ /usr/src/app/scripts/
COPY ./Setup.py /usr/src/app
COPY ./Database.py /usr/src/app
COPY ./YobotaTest.py /usr/src/app
COPY ./env /usr/src/app/env
COPY ./docker_run_mysql.sh /usr/src/app
COPY ./requirements.txt /usr/src/app
#RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN sudo apt-get install -y gcc && \
#   sudo apt-get install -y g++
RUN chmod +x /usr/src/app/docker_run_mysql.sh
RUN pip3 install -r requirements.txt --upgrade
CMD ["/usr/src/app/docker_run_mysql.sh"]
