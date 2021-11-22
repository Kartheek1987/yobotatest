#!/bin/bash

# Allow to be queried from outside
sed -i '31 s/bind-address/#bind-address/' /etc/mysql/mysql.conf.d/mysqld.cnf

service mysql start

# Create a Database, a user with password, and permissions
# cd /var/mysql_carles
# mysql -u root < start.sql

while [ true ]; do sleep 60; done
