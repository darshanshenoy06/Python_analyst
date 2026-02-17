SELECT city, SUM(amount) AS total_revenue
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY city
ORDER BY total_revenue DESC;