
SELECT p.product_id, ifnull(round(sum(price*units)/sum(units),2),0) as average_price 
FROM prices as p
left JOIN unitssold as u
on p.product_id = u.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
 GROUP BY p.product_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna