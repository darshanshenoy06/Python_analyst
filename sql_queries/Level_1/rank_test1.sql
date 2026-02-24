Select 
    user_id,
    amount,
    RANK() OVER ( ORDER BY amount DESC) AS rank_by_amount
FROM user_transactions