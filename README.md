# YOBOTA TEST

## The document outlines the set of instruction that needs to be followed as below

1. Install Docker Desktop on your local will help instaling docker compose that then lets you use docker compose commands.
2. Git clone repository `git clone git@github.com:Kartheek1987/yobotatest.git`
3. Next cd into the repository and run `docker compose up --build`
4. To log into the sql container do `docker exec --it MYSQL_db bash` and the use
   `mysql --host=mysql_db -u = root -P 3306 -p` and enter and then give the username for the root password. After `use scripts;` db and `select * from versionTable;` and `select * from testTable;` to view the data
5. The docker compose will basically spin up mysql and python app containers required for the code to run
6. Dockerfile includes all the necessary setup for install python once the docker compose is ran.
7. Env folder has the environment variables for connecting to MYSQL that are used in Setup.py python code.
8. Setup.py code has the database connection, functions that create db, create table, insert table values, select table values and the execute script that has the necessary logic as mentioned in the test.

Note : Even If the docker compose up --build exited with code 1 the tables are created and data is pushed into db , running another docker compose up --build would shows that.

Please look for logs on docker desktop for the container yobotatest
