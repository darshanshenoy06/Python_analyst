WITH ranked_txn AS (
    SELECT user_name,
           amount,
           ROW_NUMBER() OVER (PARTITION BY user_name ORDER BY amount DESC) AS rn
    FROM user_transactions
    WHERE amount IS NOT NULL
)
SELECT *
FROM ranked_txn
WHERE rn <= 2;