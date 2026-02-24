SELECT
    city,
    ROUND(
        SUM(amount) * 100.0 / SUM(SUM(amount)) OVER (),
        2
    ) AS revenue_percentage
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY city
ORDER BY revenue_percentage DESC;