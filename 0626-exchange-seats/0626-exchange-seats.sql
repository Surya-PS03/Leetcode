# Write your MySQL query statement below
WITH swapping AS(
SELECT id,student,
CASE
    WHEN id%2=1 THEN IFNULL(LEAD(student,1) OVER(ORDER BY id),student)
    WHEN id%2=0 THEN LAG(student,1) OVER(ORDER BY id)
END AS swap
FROM Seat
)

SELECT id,swap AS student
FROM swapping;
