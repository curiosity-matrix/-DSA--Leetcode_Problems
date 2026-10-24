# Write your MySQL query statement below

with temp as
(
select 
    num,
    lead(num,1) over(order by id) as nxt,
    lead(num,2) over(order by id) as secnxt
from logs
)
select distinct num as consecutiveNums
from temp
where num=nxt and
    nxt = secnxt

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna