# YOBOTA TEST

## The document outlines the set of instruction that needs to be followed as below

1. Git clone repository `git clone git@github.com:Kartheek1987/yobotatest.git`
2. Next cd into the repository and run `docker compose up --build`
3. To log into the sql container do `docker exec --it MYSQL_db bash` and the use
4. The docker compose will basically spin up mysql and python app containers required for the code to run
5. Dockerfile includes all the necessary setup for install python once the docker compose is ran.
6. Env folder has the environment variables for connecting to MYSQL that are used in Setup.py python code.
7. Setup.py code has the database connection, functions that create db, create table, insert table values, select table values and the execute script that has the necessary logic as mentioned in the test.
