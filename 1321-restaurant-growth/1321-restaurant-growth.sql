# Write your MySQL query statement below

WITH DailyTotal as (
    SELECT visited_on,SUM(amount) as daily_amount
    FROM Customer
    GROUP BY visited_on
),

RunningWindow as (
    SELECT visited_on,
    SUM(daily_amount) OVER(ORDER BY visited_on 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount,
    ROUND(
        AVG(daily_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2
    ) AS avg_amount,
    DENSE_RANK() OVER(ORDER BY visited_on) as rnk
    FROM DailyTotal
)

SELECT visited_on,amount,avg_amount as average_amount
FROM RunningWindow
WHERE rnk>=7;

