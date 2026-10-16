# Write your MySQL query statement below

    SELECT unique_id, name
    FROM employees as e
    LEFT JOIN employeeuni as ei
    on e.id = ei.id



-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna