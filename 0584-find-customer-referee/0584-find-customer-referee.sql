# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE IF(referee_id IS NOT NULL, referee_id != 2, True);