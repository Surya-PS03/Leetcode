# Write your MySQL query statement below
WITH temp AS(
SELECT id,temperature,recordDate,
LAG(temperature,1) OVER(ORDER BY recordDate ASC) AS prev_temp,
LAG(recordDate,1) OVER(ORDER BY recordDate ASC) AS prev_date
FROM Weather) 

SELECT id as ID from temp
where temperature>prev_temp
AND DATEDIFF(recordDate,prev_date)=1;