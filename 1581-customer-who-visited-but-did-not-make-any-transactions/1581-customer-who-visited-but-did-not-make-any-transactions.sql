SELECT customer_id, count(v.visit_id) as count_no_trans
FROM visits as v
left join transactions as t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by customer_id


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna