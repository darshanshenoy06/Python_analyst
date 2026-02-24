SELECT 
    user_id,
    transaction_date,
    amount,
    COALESCE(LEAD(amount) OVER(PARTITION BY user_id ORDER BY transaction_date),0) AS next_transaction_amount   
FROM user_transactions