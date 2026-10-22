# Write your MySQL query statement below
with temp as
(
    select num, count(num) as cnt
    from mynumbers
    group by num
)
select max(num) as num
from temp
where cnt=1;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna