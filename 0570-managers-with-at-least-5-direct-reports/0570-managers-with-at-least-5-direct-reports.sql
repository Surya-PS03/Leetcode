# Write your MySQL query statement below

SELECT a.name
FROM Employee a
JOIN Employee b
ON a.id = b.managerId
GROUP BY a.id
HAVING COUNT(*)>=5
;

-- use COUNT(*) instead of COUNT(b.name) b.name are null then COUNT(*) counts it 0 times.