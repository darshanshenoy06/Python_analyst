WITH transactions AS (
    SELECT 
        user_name,
        amount,
        transaction_date
    FROM user_transactions
    WHERE amount IS NOT NULL
),
ranked_transactions AS (
    SELECT 
        user_name,
        transaction_date,
        amount AS latest_amount,
        LAG(amount) OVER (
            PARTITION BY user_name 
            ORDER BY transaction_date
        ) AS previous_amount,
        ROW_NUMBER() OVER (
            PARTITION BY user_name 
            ORDER BY transaction_date DESC
        ) AS rn
    FROM transactions
)
SELECT 
    user_name,
    transaction_date AS latest_transaction_date,
    latest_amount,
    previous_amount
FROM ranked_transactions
WHERE rn = 1
  AND latest_amount > previous_amount;
