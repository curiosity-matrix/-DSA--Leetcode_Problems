# Write your MySQL query statement below
WITH start_act as
(
SELECT machine_id,activity_type as act1,sum(timestamp) as start_t,count(process_id) as cnt
FROM activity
WHERE activity_type='start'
GROUP BY machine_id
),
end_act as
(
SELECT machine_id,activity_type as act2, sum(timestamp) as end_t
FROM activity
WHERE activity_type='end'
GROUP BY machine_id
)
SELECT start_act.machine_id,round(((end_t-start_t)/cnt),3) as processing_time
FROM start_act
join end_act
on start_act.machine_id=end_act.machine_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna