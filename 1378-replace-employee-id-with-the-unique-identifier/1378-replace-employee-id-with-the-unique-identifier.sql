# Write your MySQL query statement below
select EmployeeUNI.unique_id, Employees.name 
from Employees
left outer join EmployeeUNI on EmployeeUNI.id = Employees.id;