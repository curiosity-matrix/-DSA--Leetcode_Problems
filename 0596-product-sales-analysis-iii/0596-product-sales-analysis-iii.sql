# Write your MySQL query statement below

with temp as
(SELECT product_id, min(year) as first_year
from sales
group by product_id)


SELECT temp.product_id, temp.first_year, quantity, price
FROM sales
inner join temp
on temp.first_year=sales.`year`
and temp.product_id=sales.product_id;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna