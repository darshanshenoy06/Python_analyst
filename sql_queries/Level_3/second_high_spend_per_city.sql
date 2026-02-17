;WITH user_spend AS (
    SELECT 
        city, 
        user_name, 
        SUM(amount) AS total_spend
    FROM user_transactions
    WHERE amount IS NOT NULL
    GROUP BY city, user_name
),
ranked AS (
    SELECT 
        city,
        user_name,
        total_spend,
        RANK() OVER (
            PARTITION BY city 
            ORDER BY total_spend DESC
        ) AS rnk
    FROM user_spend
)
SELECT 
    city, 
    user_name, 
    total_spend
FROM ranked
WHERE rnk = 2;
