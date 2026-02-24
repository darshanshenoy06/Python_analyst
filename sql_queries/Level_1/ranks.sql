SELECT 
    user_id,
    amount,
    rank_within_user
FROM (
    SELECT 
        user_id,
        amount,
        RANK() OVER (
            PARTITION BY user_id 
            ORDER BY amount DESC
        ) AS rank_within_user
    FROM user_transactions 
    WHERE amount IS NOT NULL
) t
WHERE rank_within_user <= 2
ORDER BY user_id, rank_within_user;