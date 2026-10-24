with temp as
(
select person_name,
sum(weight) over(order by turn) as totwt
from queue
)
select person_name
from temp 
where totwt<=1000
order by totwt desc
limit 1;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna