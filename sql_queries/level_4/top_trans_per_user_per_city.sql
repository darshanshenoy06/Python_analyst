WITH ranked_txn AS (
    SELECT city,
           user_name,
           transaction_date,
           amount,
           ROW_NUMBER() OVER (PARTITION BY city, user_name ORDER BY amount DESC) AS rn
    FROM user_transactions
    WHERE amount IS NOT NULL
)
SELECT city, user_name, transaction_date, amount
FROM ranked_txn
WHERE rn = 1;