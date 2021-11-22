FROM python:latest
LABEL authors="KartheekThamma"

# Sets the working directory to /usr/src/app and copies the local files into workdir
WORKDIR /usr/src/app
COPY ./scripts/ /usr/src/app/scripts/
COPY ./Setup.py /usr/src/app
COPY ./env /usr/src/app/env
COPY ./docker_run_mysql.sh /usr/src/app
COPY ./requirements.txt /usr/src/app

# Runs the docker_run_mysql.sh script to update the sql conf file for first time
# Also installs the necessary packages via pip
RUN chmod +x /usr/src/app/docker_run_mysql.sh
RUN pip3 install -r requirements.txt --upgrade
CMD ["/usr/src/app/docker_run_mysql.sh"]
