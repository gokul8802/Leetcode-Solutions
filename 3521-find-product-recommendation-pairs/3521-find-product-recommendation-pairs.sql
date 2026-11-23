# Write your MySQL query statement below
SELECT
    t1.product_id AS product1_id,
    t2.product_id AS product2_id,
    ip1.category AS product1_category,
    ip2.category AS product2_category,
COUNT(t1.user_id) AS customer_count
FROM ProductPurchases t1
INNER JOIN 
    ProductPurchases t2 ON t1.user_id = t2.user_id
    AND t1.product_id < t2.product_id
LEFT JOIN
    ProductInfo ip1 ON t1.product_id=ip1.product_id
LEFT JOIN
    ProductInfo ip2 ON t2.product_id=ip2.product_id
GROUP BY
    product1_id, product2_id
HAVING COUNT(t1.user_id) >= 3
ORDER BY  customer_count DESC, product1_id, product2_id
    