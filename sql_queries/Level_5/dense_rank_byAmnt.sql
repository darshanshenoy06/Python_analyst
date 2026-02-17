SELECT user_name,
       amount,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_amount
FROM user_transactions
WHERE amount IS NOT NULL;