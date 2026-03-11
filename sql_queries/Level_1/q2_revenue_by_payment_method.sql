Select 
        payment_method,
        SUM(amount) AS total_transaction_amount,
        SUM(total_fee) AS total_billing_revenue
from user_transactions
WHERE payment_method IS NOT NULL
group by payment_method
order by total_billing_revenue DESC
