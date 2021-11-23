USE SCRIPTS;
CREATE TABLE testTable3
(
  Id Integer(10) NOT NULL PRIMARY KEY,
  Script varchar2(40)
);
INSERT INTO testTable3
  (Id,Script)
VALUES
  (1,
    "testscript3.sql"
)
