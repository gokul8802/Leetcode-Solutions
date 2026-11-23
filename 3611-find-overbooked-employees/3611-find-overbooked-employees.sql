# Write your MySQL query statement below

with hours_weeks as (
select 
m.employee_id,
e.employee_name,
e.department,
sum(m.duration_hours) as total_hours
from meetings m
join employees e using(employee_id)
group by m.employee_id, e.employee_name, e.department, yearweek(meeting_date, 1)
)

select 
employee_id,
employee_name,
department,
count(*) as meeting_heavy_weeks
from hours_weeks
where total_hours > 20
group by employee_id, employee_name, department
having count(*) >= 2
order by meeting_heavy_weeks desc, employee_name;