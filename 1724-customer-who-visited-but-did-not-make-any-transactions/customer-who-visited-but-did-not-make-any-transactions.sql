-- Write your PostgreSQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits as v LEFT JOIN Transactions as t ON t.visit_id=v.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id