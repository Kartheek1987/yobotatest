USE SCRIPTS;
CREATE TABLE testTable1
(
  Id Integer(10) NOT NULL PRIMARY KEY,
  Script varchar2(40)
);
INSERT INTO testTable1
  (Id,Script)
VALUES
  (1,
    "testscript1.sql"
)
