--------------------------
---- Multiple Tables -----
--------------------------

SELECT column1, column2
FROM table_name
INNER JOIN table_name2 ON tableName1.id = tableName2.table1Id

-- LEFT JOIN

-- RIGHT JOIN

-- FULL OUTER JOIN

-- CROSS JOIN
SELECT c1, column2
FROM table_name
CROSS JOIN t2

-- or

SELECT c1, column2
FROM t1, t2

-- inner join on same table
SELECT c1, c2
FROM t1 A
INNER JOIN t1 B ON <condition> 

--------------------------
------ SQL Operators -----
--------------------------

 -- union

 SELECT c1, c2 FROM t1
 UNION [ALL]
 SELECT c1, c2 FROM t2

 -- union removes duplicates while union all does NOT
 -- union only selects distinct values
 -- if you know you don't have to dedupe, union all will give a faster result
 
 

 -- intersection - shows two queries filtering one another
 SELECT c1, c2 FROM t1
 INTERSECT
 SELECT c1, c2 FROM t2

-- minus - shows a subset of results from the original query
 SELECT c1, c2 FROM t1
 MINUS
 SELECT c1, c2 FROM t2

 -- like or Not like string match
 SELECT c1, c2 
 FROM t1
 WHERE c1 NOT LIKE [NOT LIKE] '%string%'

 -- in or not in list
 SELECT c1, c2 
 FROM t1
 WHERE c1 IN [NOT IN] (1,2,3)

-- between
SELECT c1, c2
FROM t1
WHERE c1 BETWEEN low and high

-- is null / is not null
SELECT c1, c2
FROM t1
WHERE c1 IS NULL [IS NOT NULL]


--------------
--- TABLES ---
--------------

CREATE TABLE table_name (
    id INT PRIMARY KEY,
    name VARCHAR NOT NULL
    price DECIMAL(9,2) DEFAULT 0.00
)

-- Drop Table
DROP TABLE table_name;

-- Add column
ALTER TABLE table_name ADD column1;

-- Drop column
ALTER TABLE table_name DROP COLUMN column1;

-- Add a constraint
ALTER TABLE table_name ADD constraint;

-- Drop a constraint
ALTER TABLE table_name DROP constraint;

-- Rename table
ALTER TABLE table_name ADD constraint;


----------------
----- LEAD -----
----------------

SELECT DISTINCT Num as ConsecutiveNums
FROM
    (
        SELECT Id
            , Num
            , Lead(Num, 1) OVER(ORDER BY Id) as NextNum
            , Lead(Num, 2) OVER(ORDER BY Id) as NextNum2
        FROM Logs
    ) A
WHERE Num = NextNum and Num = NextNum2


----------------
--- Triggers ---
----------------

CREATE OR MODIFY TRIGGER trigger_name
<WHEN> <EVENT>
ON table_name <TRIGGER_TYPE>
EXECUTE stored_procedure

-- WHEN - BEFORE, AFTER
-- EVENT - INSERT, UPDATE, DELETE
-- TRIGGER_TYPE - FOR EACH ROW, FOR EACH STATEMENT


---------------
--- INDEXES ---
---------------

CREATE INDEX idx_name
ON table(column1, column2)

CREATE UNIQUE INDEX idx_name
ON table(column1, column2)

DROP INDEX idx_name

-- SQL Aggregations
-- AVG
-- COUNT
-- SUM
-- MAX
-- MIN

-------------
--- VIEWS ---
-------------
CREATE VIEW v(column1, column2)
as
SELECT column2, column2
FROM table_name

-- view with check option

CREATE VIEW v(column1, column2)
as
SELECT column2, column2
FROM table_name
WITH [CASCADED | LOCAL] CHECK OPTION

-- recursive view

CREATE VIEW v(column1, column2)
as
select-STATEMENT
UNION [ALL]
select-statement;

-- temporary view

CREATE TEMPORARY VIEW v
AS 
SELECT column2, column2
FROM table_name

-- drop view

DROP VIEW view_name;

