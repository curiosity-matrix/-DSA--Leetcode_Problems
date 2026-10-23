with temp as
(
select reports_to, count(reports_to) as reports_count, round(avg(age),0) as average_age
from employees
group by reports_to
having reports_count>=1
)
select employee_id, name, reports_count, average_age
from employees
inner join temp
on employee_id = temp.reports_to
order by employee_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna