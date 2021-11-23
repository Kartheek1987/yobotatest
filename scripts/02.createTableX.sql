USE SCRIPTS;
CREATE TABLE testTable2
(
  Id Integer(10) NOT NULL PRIMARY KEY,
  Script varchar2(40)
);
INSERT INTO testTable2
  (Id,Script)
VALUES
  (1,
    "testscript2.sql"
)
