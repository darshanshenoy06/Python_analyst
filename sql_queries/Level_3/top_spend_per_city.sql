WITH ranked_users AS (
    SELECT city,
           user_name,
           SUM(amount) AS total_spend,
           ROW_NUMBER() OVER (PARTITION BY city ORDER BY SUM(amount) DESC) AS rn
    FROM user_transactions
    WHERE amount IS NOT NULL
    GROUP BY city, user_name
)
SELECT city, user_name, total_spend
FROM ranked_users
WHERE rn = 1;