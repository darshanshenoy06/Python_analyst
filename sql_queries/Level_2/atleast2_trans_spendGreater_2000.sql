SELECT user_name,
       SUM(amount) AS total_spend,
       COUNT(transaction_id) AS transaction_count
FROM user_transactions
GROUP BY user_name
HAVING SUM(amount) > 2000
   AND COUNT(transaction_id) >= 2;