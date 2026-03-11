-- This file is to check the data of the table whenever we CREATE UPDATE or DELETE something from the table.
Select * 
from user_transactions 
where signup_date >= '2026-01-01'
order by user_id ASC 