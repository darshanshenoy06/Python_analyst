WITH ranked_txn AS (
    SELECT user_name,
           transaction_date,
           amount,
           ROW_NUMBER() OVER (PARTITION BY user_name ORDER BY transaction_date DESC) AS rn
    FROM user_transactions
    WHERE amount IS NOT NULL
)
SELECT user_name, transaction_date, amount
FROM ranked_txn
WHERE rn = 1;