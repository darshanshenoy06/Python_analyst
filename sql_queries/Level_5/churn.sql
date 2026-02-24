SELECT 
        user_id,
        transaction_date,
        amount,
        COALESCE(
            LEAD(transaction_date)
            OVER(PARTITION BY user_id
            ORDER BY transaction_date), '9999-12-31') 
            AS next_transaction_date,
            CASE 
                WHEN COALESCE(LEAD(transaction_date)
            OVER(PARTITION BY user_id
            ORDER BY transaction_date), '9999-12-31') 
            IS NULL THEN 'Churn Risk'
            ELSE 'Active'
            END AS churn_flag
FROM user_transactions
ORDER BY user_id, transaction_date;
