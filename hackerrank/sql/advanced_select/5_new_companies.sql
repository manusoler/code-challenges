-- Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 
-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.
-- Note:
-- The tables may contain duplicate records.
-- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

select c.company_code, c.founder, num_lm, num_sm, num_m, num_e
from company c
    join (
        select c1.company_code, count(*) as num_lm
        from (
            select distinct c1.company_code, lm.lead_manager_code
            from company c1 
                join Lead_Manager lm on c1.company_code = lm.company_code
        ) c1
        group by c1.company_code
    ) lm on lm.company_code = c.company_code
    join (
        select c1.company_code, count(*) as num_sm
        from (
            select distinct c1.company_code, sm.senior_manager_code
            from company c1 
                join Lead_Manager lm on c1.company_code = lm.company_code
                join Senior_Manager sm on lm.lead_manager_code = sm.lead_manager_code
        ) c1
        group by c1.company_code
    ) sm on sm.company_code = c.company_code
    join (
        select c1.company_code, count(*) as num_m
        from (
            select distinct c1.company_code, m.manager_code
            from company c1 
                join Lead_Manager lm on c1.company_code = lm.company_code
                join Senior_Manager sm on lm.lead_manager_code = sm.lead_manager_code
                join Manager m on sm.senior_manager_code = m.senior_manager_code
        ) c1
        group by c1.company_code
    ) m on m.company_code = c.company_code
    join (
        select c1.company_code, count(*) as num_e
        from (
            select distinct c1.company_code, e.employee_code
            from company c1 
                join Lead_Manager lm on c1.company_code = lm.company_code
                join Senior_Manager sm on lm.lead_manager_code = sm.lead_manager_code
                join Manager m on sm.senior_manager_code = m.senior_manager_code
                join Employee e on m.manager_code = e.manager_code
        ) c1
        group by c1.company_code
    ) e on e.company_code = c.company_code
order by company_code;