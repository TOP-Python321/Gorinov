-- Запросы к таблице doctors:

-- 1. Вывести средний оклад (salary) всех сотрудников
select avg(salary) as 'Средний оклад'
from doctors;

-- +---------------+
-- | Средний оклад |
-- +---------------+
-- |  72767.671429 |
-- +---------------+
-- 1 row in set (0.0004 sec)

-----------------------------------------------------------------------------------------------------------------
-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата 
-- предыдущего запроса)
select avg(premium) as 'Средняя премия'
from doctors
where salary > 72767.671429;

-- +----------------+
-- | Средняя премия |
-- +----------------+
-- |   21681.382353 |
-- +----------------+
-- 1 row in set (0.0004 sec)

-------------------------------------------------------------------------------------------------------------------
-- Запросы к таблице vacations:

-- 3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника — используйте 
-- функцию datediff()
select avg(datediff(end_date, start_date)) as `Среднеe количество дней в отпуске`
  from vacations
 group by doctors_id
 order by `Среднеe количество дней в отпуске`;

-- вариант с выводом ФИО врачей
 -- select concat_ws(' ', last_name, first_name, patr_name) as `врач`, 
       -- avg(datediff(end_date, start_date)) as `Среднеe количество дней в отпуске`
  -- from vacations as v
  -- join doctors as d
    -- on v.doctors_id = d.id
 -- group by doctors_id
 -- order by `Среднеe количество дней в отпуске`;

-- +-----------------------------------+
-- | Среднеe количество дней в отпуске |
-- +-----------------------------------+
-- |                         1796.2222 |
-- |                         1884.1333 |
-- |                         2158.8000 |
-- |                         2159.8333 |
-- |                         2160.3636 |
-- .......................................
-- |                         3664.9091 |
-- |                         3739.1667 |
-- |                         3781.5455 |
-- |                         3788.6111 |
-- |                         3870.0000 |
-- |                         4893.7500 |
-- +-----------------------------------+
-- 70 rows in set (0.0015 sec)

-----------------------------------------------------------------------------------------------------------------
-- 4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по 
-- возрастанию разности между этими двумя значениями 
select min(year(start_date)) as `ранний год`,
       max(year(end_date)) as `поздний год`
  from vacations  
 group by doctors_id
 order by `поздний год` - `ранний год`;

-- select concat_ws(' ', last_name, first_name, patr_name) as `врач`, 
       -- min(year(start_date)) as `мин год`,
       -- max(year(end_date)) as `мак год`
  -- from vacations as v
  -- join doctors as d
    -- on v.doctors_id = d.id
 -- group by doctors_id
 -- order by `мак год` - `мин год`;
 
-- +------------+-------------+
-- | ранний год | поздний год |
-- +------------+-------------+
-- |       2002 |        2021 |
-- |       2002 |        2022 |
-- |       2001 |        2021 |
-- |       2001 |        2022 |
-- .............................
-- |       2000 |        2024 |
-- |       2000 |        2024 |
-- |       2000 |        2024 |
-- +------------+-------------+
-- 70 rows in set (0.0015 sec)

----------------------------------------------------------------------------------------------------------------------------
-- Запросы к таблице donations:

-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений
select sum(amount) as `Сумма пожертвований`
  from donations
 group by departments_id
 order by departments_id;

-- вариант с выводом отделений
-- select dep.department as `Отделение`, 
      -- sum(amount) as `Сумма пожертвований`
  -- from donations as don
  -- join departments as dep
    -- on don.departments_id = dep.id
 -- group by departments_id
 -- order by departments_id;

-- +---------------------+
-- | Сумма пожертвований |
-- +---------------------+
-- |          3906387.00 |
-- |         14824812.00 |
-- |          5329716.00 |
-- |         17541590.00 |
-- |         18834643.00 |
-- |          8932248.00 |
-- |          3288830.00 |
-- +---------------------+
-- 7 rows in set (0.0005 sec)

--------------------------------------------------------------------------------------------------------------------------- 
-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов
select sum(amount) as `Сумма пожертвований`
from donations
group by sponsors_id, date 
order by sponsors_id, date;

-- +---------------------+
-- | Сумма пожертвований |
-- +---------------------+
-- |            34539.00 |
-- |          1996781.00 |
-- |           245080.00 |
-- ........................
-- |           127413.00 |
-- |          1870133.00 |
-- +---------------------+
-- 70 rows in set (0.0005 sec)