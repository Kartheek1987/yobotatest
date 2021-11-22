from typing import OrderedDict
import mysql.connector
from mysql.connector import errorcode
import os
from pathlib import Path
import collections
from collections import OrderedDict

# from Database import cursor
from dotenv import load_dotenv, find_dotenv

# This loads the environment variables into this file
load_dotenv(find_dotenv())

# global variables
fileNames = []
fileNameDict = {}
global dbVersion

# specify database configurations
db_user = os.getenv('MYSQL_USER')
db_pwd = os.getenv('MYSQL_ROOT_PASSWORD')
db_host = os.getenv('MYSQL_HOST_NAME')
db_name = os.getenv('MYSQL_DATABASE')

mydb = mysql.connector.connect(
    user=db_user,
    password=db_pwd,
    host=db_host,
    database=db_name
)

my_cursor = mydb.cursor()
DB_NAME = 'scripts'
TABLES = {}

TABLES['versionTable'] = (
    "CREATE TABLE `versionTable` ("
    " `Id` int(11) NOT NULL AUTO_INCREMENT,"
    " `version` int(11) NOT NULL,"
    " PRIMARY KEY (`Id`)"
    ") ENGINE=InnoDB"
)


def create_database():
    my_cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Created {} database".format(DB_NAME))


def create_tables():
    my_cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_desc = TABLES[table_name]
        try:
            print("Creating Table ({}) ".format(table_name), end="")
            my_cursor.execute(table_desc)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table Already Exists")
            else:
                print(err.msg)


def show_tables():
    my_cursor.execute("USE {}".format(DB_NAME))
    sql = ("SELECT version FROM versionTable")
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for dbVersion in result:
        return dbVersion[0]
        #print("Existing db_version is ", dbVersion[0])


def execute_Scripts(dbver):
    path = Path("scripts")

    for p in path.iterdir():
        result = p.name.endswith('.sql')
        if result == True:
            fileNameOnly = p.name.replace(' ', '.')
            if fileNameOnly[0].isdigit() == True:
                fileNumber = fileNameOnly.split('.')
                fileNameDict[fileNumber[0]] = p.name
                sortedFileNoDict = dict(sorted(fileNameDict.items()))
    print(sortedFileNoDict)

    # lastkey = int((reversed(sortedFileNoDict.keys())))
    lastkey = int(list(sortedFileNoDict.keys())[-1])
    print(lastkey)
    if int(dbver) == lastkey:
        print("This scripts are using the latest db version which is", lastkey)
        print("Reversed range of key", list(reversed(range(lastkey+1))))
    elif int(dbver) < lastkey:
        for k, v in sortedFileNoDict.items():
            if sortedFileNoDict[k] > str(dbver):
                print(sortedFileNoDict[k])


create_database()
create_tables()
show_tables()
execute_Scripts(dbver=show_tables())
