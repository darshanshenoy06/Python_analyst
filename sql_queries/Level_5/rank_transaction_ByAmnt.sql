SELECT user_name,
       amount,
       RANK() OVER (ORDER BY amount DESC) AS rank_by_amount
FROM user_transactions
WHERE amount IS NOT NULL;