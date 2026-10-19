SELECT date_format(trans_date,'20%y-%m') as `month`, country, count(*) as trans_count, sum(state='approved') as approved_count, sum(amount) as trans_total_amount, 
SUM(
    CASE

    when state='approved' then amount
    else 0

end) as approved_total_amount
FROM transactions
GROUP BY month,country

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna