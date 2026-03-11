SELECT 
    DATEFROMPARTS(YEAR(transaction_date),
    MONTH(transaction_date), 1) AS revenue_month,
    SUM(total_fee) AS total_billing_revenue
FROM user_transactions 
WHERE transaction_date IS NOT NULL
GROUP BY DATEFROMPARTS(YEAR(transaction_date), MONTH(transaction_date), 1)
ORDER BY revenue_month ASC;