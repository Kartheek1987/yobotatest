FROM python:latest
LABEL authors="KartheekThamma"

# Created workdir and copy the files from local to the workinng directory
EXPOSE 3306
WORKDIR /usr/src/app
COPY ./scripts/ /usr/src/app/scripts/
COPY ./Setup.py /usr/src/app
COPY ./env /usr/src/app/env
COPY ./docker_run_mysql.sh /usr/src/app
COPY ./requirements.txt /usr/src/app

# Run the first docker_run_mysql.sh to set up sql config file and then install python packages
RUN chmod +x /usr/src/app/docker_run_mysql.sh
RUN pip3 install -r requirements.txt --upgrade
CMD ["/usr/src/app/docker_run_mysql.sh"]
