-- Query the difference between the maximum and minimum populations in CITY.
select (select max(population) from city) - (select min(population) from city) from dual;