SELECT category, SUM(amount) AS total_revenue
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY category
ORDER BY total_revenue DESC;