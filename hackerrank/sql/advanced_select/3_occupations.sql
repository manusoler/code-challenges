-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
-- Note: Print NULL when there are no more names corresponding to an occupation.
select doctor, professor, singer, actor
from (
    select * from (
        select Name, occupation, 
            (ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name)) as row_num 
        from occupations 
        order by name asc
    ) 
    pivot ( 
        min(name)
        for occupation 
        in ('Doctor' as doctor,'Professor' as professor,'Singer' as singer,'Actor' as actor)
    )
    order by row_num
);