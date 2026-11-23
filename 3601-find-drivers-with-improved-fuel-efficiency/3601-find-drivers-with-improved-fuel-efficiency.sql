# Write your MySQL query statement below
with cte as (
    select 
        d.driver_id,
        d.driver_name,
        avg(t.distance_km / t.fuel_consumed) as first_half_avg
    from trips as t 
    join drivers as d on d.driver_id = t.driver_id 
    where month(trip_date) in(1,2,3,4,5,6) 
    group by d.driver_id
), 
cte1 as (
    select 
        cte.driver_id,
        cte.driver_name,
        cte.first_half_avg,
        avg(t.distance_km / t.fuel_consumed) as second_half_avg
    from trips as t 
    join cte on cte.driver_id = t.driver_id 
    where month(t.trip_date) in(7,8,9,10,11,12) 
    group by cte.driver_id)
select 
    driver_id,
    driver_name,
    round(first_half_avg,2) as first_half_avg,
    round(second_half_avg,2) as second_half_avg,
    round(second_half_avg - first_half_avg, 2) as efficiency_improvement
from cte1 
where (cte1.second_half_avg-cte1.first_half_avg)>0
order by efficiency_improvement desc, driver_name asc;