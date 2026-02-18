with user_spend AS (   
    SELECT 
        city,
        user_name,
        SUM(amount) AS total_spend
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY city, user_name
),
ranked_users AS (
    SELECT city,
        user_name,
        total_spend,
        DENSE_RANK() OVER (PARTITION BY city ORDER BY total_spend DESC) AS rank_in_city
    FROM user_spend
)
SELECT 
    city,
    user_name,
    total_spend,
    rank_in_city
FROM ranked_users

WHERE rank_in_city <= 2
ORDER BY city,total_spend DESC;