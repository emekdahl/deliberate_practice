SELECT d.Name AS Department
    , e.Name AS Employee
    , e.Salary
FROM Department d, Employee e
WHERE d.Id = e.DepartmentId
    AND (
        SELECT COUNT(DISTINCT Salary)
        FROM Employee
        WHERE DepartmentId = d.Id
            AND Salary > e.Salary
    ) < 3
    