SELECT city,
       user_name,
       amount,
       RANK() OVER (PARTITION BY city ORDER BY amount DESC) AS city_rank
FROM user_transactions
WHERE amount IS NOT NULL;