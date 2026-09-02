# Write your MySQL query statement below

SELECT a.machine_id, ROUND(AVG(ABS(a.timestamp-b.timestamp)),3) AS processing_time
FROM Activity a

JOIN Activity b

ON (a.machine_id,a.process_id) = (b.machine_id,b.process_id)

WHERE a.activity_type <> b.activity_type AND a.activity_type!="start"
GROUP BY machine_id;