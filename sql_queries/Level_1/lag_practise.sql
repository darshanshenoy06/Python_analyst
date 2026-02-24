SELECT 
    user_id,
    transaction_date,
    amount,
    COALESCE(LAG(amount) OVER (PARTITION BY user_id ORDER BY transaction_date),0) AS previous_transaction_amount
FROM user_transactions
ORDER BY user_id, transaction_date;