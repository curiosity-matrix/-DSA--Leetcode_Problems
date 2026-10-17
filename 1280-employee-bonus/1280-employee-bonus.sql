# Write your MySQL query statement below
SELECT e.name,b.bonus
FROM employee as e
left join bonus as b
on e.empid = b.empid
where b.bonus<1000 or b.bonus is null

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna