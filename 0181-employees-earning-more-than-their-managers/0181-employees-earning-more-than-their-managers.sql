# Write your MySQL query statement below
SELECT name as Employee from(SELECT E1.id,E1.name,E1.salary,E2.salary as manSalary from
Employee E1
JOIN Employee E2
ON E1.managerID=E2.id) m
WHERE salary>manSalary;