SELECT user_name,
       amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num
FROM user_transactions
WHERE amount IS NOT NULL;