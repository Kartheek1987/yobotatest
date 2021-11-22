#!/bin/bash

# Allow to be queried from outside
sed -i '31 s/bind-address/#bind-address/' /etc/mysql/mysql.conf.d/mysqld.cnf

service mysql start

while [ true ]; do sleep 60; done
