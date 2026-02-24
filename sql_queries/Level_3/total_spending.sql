SELECT 
    user_id,
    transaction_date,
    amount,
    SUM(amount) OVER (PARTITION BY user_id) AS total_spending
FROM user_transactions
WHERE amount IS NOT NULL
ORDER BY user_id, transaction_date;