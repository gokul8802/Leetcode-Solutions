# Write your MySQL query statement below
WITH tmp AS(
    SELECT
        p.employee_id,
        e.name,
        p.review_date,
        rating,
        ROW_NUMBER() OVER(
            PARTITION BY p.employee_id ORDER BY p.review_date DESC
        ) AS rn,
        LAG(rating, 1) OVER(
            PARTITION BY p.employee_id ORDER BY p.review_date DESC
        ) AS first,
        LAG(rating, 2) OVER(
            PARTITION BY p.employee_id ORDER BY p.review_date DESC
        ) AS second
    FROM employees e
    INNER JOIN performance_reviews p
    ON e.employee_id = p.employee_id
)

SELECT 
    employee_id,
    name,
    second - rating AS improvement_score 
FROM tmp
WHERE
    rn = 3 AND 
    rating < first AND 
    first < second
ORDER BY improvement_score DESC, name ASC