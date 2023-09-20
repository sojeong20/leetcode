# Write your MySQL query statement below
select W1.id
from Weather as W1
left outer join Weather W2 on W2.recordDate = date_sub(W1.recordDate, interval 1 day)
where W1.temperature > W2.temperature