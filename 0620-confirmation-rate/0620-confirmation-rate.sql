with temp as
(
SELECT s.user_id, c.action
FROM signups as s
LEFT JOIN confirmations as c
ON s.user_id = c.user_id
)

SELECT user_id, round(coalesce(avg(action='confirmed'),0),2) as confirmation_rate
FROM temp
GROUP BY user_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna