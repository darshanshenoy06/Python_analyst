SELECT user_name, SUM(amount) AS total_spend
FROM user_transactions
GROUP BY user_name
HAVING SUM(amount) > 2000;