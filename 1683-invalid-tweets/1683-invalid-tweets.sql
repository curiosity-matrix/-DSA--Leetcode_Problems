# Write your MySQL query statement below

WITH temp as(
    SELECT tweet_id , content , LENGTH(content) as len
    FROM tweets
)
SELECT tweet_id
FROM temp
WHERE len>15;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna