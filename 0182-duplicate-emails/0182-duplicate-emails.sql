# Write your MySQL query statement below
SELECT Email FROM(SELECT Email,Count(Email) as C from Person
GROUP BY Email) m
WHERE C>1;