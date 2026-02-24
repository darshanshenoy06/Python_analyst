select 
    user_id,
    transaction_date,
    COALESCE(
        LEAD(transaction_date)
        OVER (PARTITION BY user_id ORDER BY transaction_date),
        '1900-01-01') AS next_transaction_date,
    DATEDIFF(
        DAY,
        transaction_date,
        COALESCE(
            LEAD(transaction_date)
            OVER (PARTITION BY user_id ORDER BY transaction_date),
            '2024-01-01')) AS days_between_transactions   
from user_transactions
WHERE transaction_date is NOT NULL
order by user_id, transaction_date;    