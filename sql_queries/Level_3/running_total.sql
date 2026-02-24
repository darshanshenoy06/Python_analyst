SELECT 
    user_id,
    transaction_date,
    amount,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY transaction_date) AS running_total
FROM user_transactions
WHERE amount IS NOT NULL
ORDER BY user_id, transaction_date;