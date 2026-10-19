# Write your MySQL query statemnt below
SELECT project_id,round(avg(e.experience_years),2) as average_years
FROM project as p
left join employee as e
on p.employee_id = e.employee_id
GROUP BY project_id



-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna