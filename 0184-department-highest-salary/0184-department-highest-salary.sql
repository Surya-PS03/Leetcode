# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM
(SELECT Department, Employee, Salary,
RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) as rnk
FROM
(SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee E
JOIN Department D
ON E.departmentId=D.id) m
) t
WHERE rnk=1;