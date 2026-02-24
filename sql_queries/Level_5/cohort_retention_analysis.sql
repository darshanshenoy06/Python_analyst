SELECT 
    user_id,
    transaction_date,
    transaction_number,
    CASE 
        WHEN transaction_number = 1 THEN 'New User'
        ELSE 'Repeat User'
    END AS user_type
FROM (
    SELECT 
        user_id,
        transaction_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id 
            ORDER BY transaction_date
        ) AS transaction_number
    FROM user_transactions
) t
ORDER BY user_id, transaction_date;