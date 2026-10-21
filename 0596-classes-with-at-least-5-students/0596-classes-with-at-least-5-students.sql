# Write your MySQL query statement below

SELECT class
FROM (
    SELECT class,count(student) as cnt
    from courses
    group by class
    having count(student) >=5
) as result

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna