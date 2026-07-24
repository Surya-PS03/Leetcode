# Write your MySQL query statement below
SELECT C.name as customers
FROM Customers C
LEFT JOIN Orders O
ON C.id=O.customerId
where O.id IS NULL;