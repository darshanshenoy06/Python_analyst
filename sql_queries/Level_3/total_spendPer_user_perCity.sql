SELECT city, user_name, SUM(amount) AS total_spend
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY city, user_name;