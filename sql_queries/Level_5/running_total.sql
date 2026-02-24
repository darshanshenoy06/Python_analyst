SELECT 
    user_id,
    transaction_date,
    amount,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY transaction_date) AS running_total_per_user
FROM user_transactions
WHERE transaction_date IS NOT NULL
