# Write your MySQL query statement below
SELECT query_name , round(avg(rating/`position`),2) as quality,
round(avg(rating<3)*100,2) as poor_query_percentage
FROM queries
GROUP BY query_name

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna