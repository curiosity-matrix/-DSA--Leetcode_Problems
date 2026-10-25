with temp as
(
select user_id, count(rating) as cnt
from movierating 
group by user_id
),


temp1 as 
(
    select movie_id,avg(rating) as average
    from movierating
    where date_format(movierating.created_at,"%Y-%m")="2020-02"
    group by movie_id
)

(
select users.name as results
from temp
inner join users
on temp.user_id = users.user_id
order by temp.cnt desc, users.name asc
limit 1
)
UNION ALL
(
select movies.title
from temp1
inner join movies
on temp1.movie_id=movies.movie_id
order by temp1.average desc,movies.title asc
limit 1
)

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna