select "Low Salary" as category,
sum(income<20000) as accounts_count
from accounts

UNION

select "Average Salary" as category,
sum(income between 20000 and 50000) as account_count
from accounts

UNION

Select "High Salary"as category,
sum(income>50000) as account_count
from accounts


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna