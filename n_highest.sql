CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN ( SELECT DISTINCT Salary FROM
      (SELECT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) as rnk
      FROM Employee) aa
          WHERE rnk = N
        );
END