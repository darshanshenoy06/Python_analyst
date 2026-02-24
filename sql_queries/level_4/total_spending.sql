SELECT 
    user_id,
    amount,
    SUM(amount) OVER(PARTITION BY user_id) AS total_spending
FROM user_transactions
WHERE amount IS NOT NULL