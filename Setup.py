from typing import OrderedDict
import mysql.connector
from mysql.connector import cursor
from mysql.connector import errorcode
import os
from pathlib import Path
import collections
from collections import OrderedDict
from mysql.connector.errors import OperationalError
from dotenv import load_dotenv, find_dotenv

# This loads the environment variables into this file
load_dotenv(find_dotenv())

# global variables
fileNames = []
fileNameDict = {}
global dbVersion

# specify database configurations from env variables
db_user = os.getenv('MYSQL_USER')
db_pwd = os.getenv('MYSQL_ROOT_PASSWORD')
db_host = os.getenv('MYSQL_HOST_NAME')
db_name = os.getenv('MYSQL_DATABASE')

# mysql connector to setup connection to db, use env variables
mydb = mysql.connector.connect(
    user=db_user,
    password=db_pwd,
    host=db_host,
    database=db_name
)


# Initializations to cursor, db name annd tables
my_cursor = mydb.cursor()
DB_NAME = 'scripts'
TABLES = {}

# Table names can be added here
TABLES['versionTable'] = (
    "CREATE TABLE `versionTable` ("
    " `Id` int(11) NOT NULL AUTO_INCREMENT,"
    " `version` int(11) NOT NULL,"
    " PRIMARY KEY (`Id`)"
    ") ENGINE=InnoDB"
)

TABLES['testTable'] = (
    "CREATE TABLE `testTable` ("
    " `Id` int(11) NOT NULL AUTO_INCREMENT,"
    " `script` varchar(50) NOT NULL,"
    " PRIMARY KEY (`Id`)"
    ") ENGINE=InnoDB"
)

# Function creates database only if it doesn't exists


def create_database():
    my_cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Created {} database".format(DB_NAME))


# Function that creates tables versionTable and testTable


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

# Function that inserts data into versionTable


def insert_data(Id, version):
    my_cursor.execute("USE {}".format(DB_NAME))
    my_cursor.execute("SELECT COUNT(*) FROM versionTable")
    rowcount = my_cursor.fetchone()
    print("The row count is ", rowcount[0])
    if rowcount[0] == 0:
        sql = ("INSERT INTO versionTable(Id, version) VALUES(%s, %s)")
        my_cursor.execute(sql, (Id, version))
        mydb.commit()
    else:
        print("Table values are already updated")

# Function that executes if the db version is lesser than the SQL file versions


def run_scripts(scriptname):
    # my_cursor.execute("USE {}".format(DB_NAME))
    sql = ("INSERT INTO testTable(script) VALUES(%s)")
    my_cursor.execute(sql, (scriptname,))
    mydb.commit()
    print("Added script {}".format(scriptname))

# Function to give version number


def show_tables():
    my_cursor.execute("USE {}".format(DB_NAME))
    sql = ("SELECT version FROM versionTable")
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for dbVersion in result:
        return dbVersion[0]

# Function updates the versionTable with the latest version from Scripts Directory


def update_tables(dbVer):
    my_cursor.execute("USE {}".format(DB_NAME))
    sql = ("UPDATE versionTable SET version = %s WHERE Id = %s")
    my_cursor.execute(sql, (dbVer, 1))
    mydb.commit()
    print("The updated version is", dbVer)
    show_tables()


# Function with the business logic that takes the scripts names &
#  provides them to subsequent functions


def execute_scripts(dbver):
    try:
        path = Path("scripts")
        for p in path.iterdir():
            result = p.name.endswith('.sql')
            if result == True:
                fileNameOnly = p.name.replace(' ', '.')
                if fileNameOnly[0].isdigit() == True:
                    fileNumber = fileNameOnly.split('.')
                    for file in fileNumber:
                        if fileNumber[0].startswith('0'):
                            fileNumber[0] = fileNumber[0].replace('0', '.')
                            fileNameDict[fileNumber[0]] = p.name
                        else:
                            fileNameDict[fileNumber[0]] = p.name
                    sortedFileNoDict = dict(sorted(fileNameDict.items()))

        lastkey = float(list(sortedFileNoDict.keys())[-1])
        if float(dbver) == lastkey:
            print("Nothing to execute because the version in db is latest", lastkey)
        elif float(dbver) < lastkey:
            for key, value in sortedFileNoDict.items():
                if float(key) > float(dbver):
                    print("The the scripts are run", key, value)
                    update_tables(int(key))
                    run_scripts(value)
    except OperationalError as err:
        print("The path could not be found", err)


# Calling All Functions for db, tables , creating tables, select and executing the logic
create_database()
create_tables()
insert_data(Id=1, version=3)
show_tables()
execute_scripts(dbver=show_tables())
