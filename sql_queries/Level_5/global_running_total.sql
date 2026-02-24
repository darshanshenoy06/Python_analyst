SELECT 
    transaction_date,
    amount,
    SUM(amount) OVER (ORDER BY transaction_date) AS global_running_total

FROM user_transactions
WHERE amount IS NOT NULL
