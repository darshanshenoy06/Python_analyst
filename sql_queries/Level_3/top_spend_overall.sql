SELECT
    user_name, 
    SUM(amount) AS total_spend
FROM user_transactions
GROUP BY user_name
ORDER BY total_spend DESC
LIMIT 1
