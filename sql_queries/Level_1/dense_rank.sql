SELECT 
    user_id,
    amount,
    DENSE_RANK() OVER ( ORDER BY amount DESC) AS dense_rank_by_amount
FROM user_transactions 
where amount is not null  