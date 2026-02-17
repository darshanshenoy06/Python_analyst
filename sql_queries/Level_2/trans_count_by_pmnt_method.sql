SELECT payment_method, COUNT(transaction_id) AS transaction_count
FROM user_transactions
WHERE amount IS NOT NULL
GROUP BY payment_method
ORDER BY transaction_count DESC;