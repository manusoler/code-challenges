-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, 
-- but did not realize her keyboard's 0 key was broken until after completing the calculation. 
-- She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.
-- Write a query calculating the amount of error (i.e.: actual - miscalculaed average monthly salaries), and round it up to the next integer.

-- Sol 1: select ceil((select avg(salary) from employees) - (select avg(to_number(replace(to_char(salary), '0', ''))) from employees)) from dual;
-- Sol 2
select ceil(avg(e.salary) - avg(e2.salary)) 
from employees e 
    join (
        select id, name, to_number(replace(to_char(salary), '0', '')) as salary 
        from employees
    ) e2 on e2.id = e.id;