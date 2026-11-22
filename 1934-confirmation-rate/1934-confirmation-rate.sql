# Write your MySQL query statement below
SELECT 
    user_id,
    ROUND(SUM(flag) / COUNT(*), 2) confirmation_rate 
FROM (
    SELECT 
        s.user_id,
        CASE 
            WHEN action IS NULL THEN 0
            WHEN action = 'timeout' THEN 0
            ELSE 1
        END flag
    FROM Signups s
    LEFT JOIN Confirmations c
        ON s.user_id = c.user_id
) t
GROUP BY user_id
ORDER BY ROUND(SUM(flag) / COUNT(*), 2);