SELECT Employee.Name as Employee
FROM Employee
LEFT JOIN (SELECT * FROM Employee) others ON others.Id = Employee.ManagerId
WHERE others.Salary < Employee.Salary