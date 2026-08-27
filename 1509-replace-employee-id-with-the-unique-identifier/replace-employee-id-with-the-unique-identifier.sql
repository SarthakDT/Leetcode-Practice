-- Write your PostgreSQL query statement below
SELECT unique_id,name
FROM EmployeeUNI AS EU RIGHT JOIN Employees AS E ON E.id=EU.id
 