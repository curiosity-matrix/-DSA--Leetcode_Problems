# Write your MySQL query statement below
with temp as
(SELECT count(*) as cnt
FROM users)

SELECT contest_id, round((((count(user_id))/cnt) * 100),2) as percentage
FROM register
join temp
GROUP BY contest_id
ORDER BY percentage desc, contest_id asc

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna