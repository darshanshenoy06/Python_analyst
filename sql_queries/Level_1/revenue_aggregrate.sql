SELECT 
    SUM(amount) AS total_revenue
FROM user_transactions
HAVING SUM(amount) is NOT NULL;