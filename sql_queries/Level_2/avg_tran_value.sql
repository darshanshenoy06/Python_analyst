SELECT AVG(amount) AS avg_transaction_value
FROM user_transactions
WHERE amount IS NOT NULL;