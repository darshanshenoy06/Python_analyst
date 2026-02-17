SELECT user_name, SUM(amount) AS total_spend
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY user_name;