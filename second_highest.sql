SELECT MAX(Employee.Salary) as SecondHighestSalary
FROM Employee
WHERE Employee.Salary < (
    SELECT MAX(Employee.Salary) 
               FROM Employee)
