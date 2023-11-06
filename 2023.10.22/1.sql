-- Запросы к таблице country

-- 1. Вывести названия всех стран Евразии
select name as Страны
  from country
 where continent in ('Europe', 'Asia');
 
 -- +-------------------------------+
-- | Страны                        |
-- +-------------------------------+
-- | Afghanistan                   |
-- | Albania                       |
-- | Andorra                       |
-- | ..............................
-- | Vietnam                       |
-- | Yemen                         |
-- | Yugoslavia                    |
-- +-------------------------------+
-- 97 rows in set (0.0005 sec)

---------------------------------------------------------------------------------------------------------------------
-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select region as Регион,
       name as Страны
  from country
 where LifeExpectancy < 50;
 
-- +---------------------------+---------------------------------------+
-- | Регион                    | Страны                                |
-- +---------------------------+---------------------------------------+
-- | Southern and Central Asia | Afghanistan                           |
-- | Central Africa            | Angola                                |
-- | Eastern Africa            | Burundi                               |
-- |.................................................................  |
-- | Southeast Asia            | East Timor                            |
-- | Eastern Africa            | Uganda                                |
-- | Eastern Africa            | Zambia                                |
-- | Eastern Africa            | Zimbabwe                              |
-- +---------------------------+---------------------------------------+
-- 28 rows in set (0.0007 sec)

--------------------------------------------------------------------------------------------------------------------------
-- 3. Вывести название самой крупной по площади страны Африки
  select name as Страна
    from country
   where continent = "Africa"
order by SurfaceArea desc
   limit 1;
-- вариант с подзапросом
-- select name as Страна
  -- from country
 -- where SurfaceArea = (select max(SurfaceArea) from country where continent = "Africa");

-- +--------+
-- | Страна |
-- +--------+
-- | Sudan  |
-- +--------+
-- 1 row in set (0.0006 sec)

--------------------------------------------------------------------------------------------------------------------------
-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
  select name as Страна
    from country
   where continent = "Asia"
order by population
   limit 5;

-- +----------+
-- | Страна |
-- +----------+
-- | Maldives |
-- | Brunei   |
-- | Macao    |
-- | Qatar    |
-- | Bahrain  |
-- +----------+
-- 5 rows in set (0.0005 sec)

--------------------------------------------------------------------------------------------------------------------------
-- Запросы к таблице city

-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять 
-- миллионов человек
  select countrycode as 'Код страны', name as 'Город'
    from city
   where population > 5000000
order by population;

-- +------------+-------------------+
-- | Код страны | Город             |
-- +------------+-------------------+
-- | PAK        | Lahore            |
-- | COD        | Kinshasa          |
-- | CHN        | Tianjin           |
-- | BRA        | Rio de Janeiro    |
-- | COL        | Santafé de Bogotá |
-- | THA        | Bangkok           |
-- | CHN        | Chongqing         |
-- | PER        | Lima              |
-- | IRN        | Teheran           |
-- | EGY        | Cairo             |
-- | IND        | Delhi             |
-- | GBR        | London            |
-- | CHN        | Peking            |
-- | JPN        | Tokyo             |
-- | USA        | New York          |
-- | RUS        | Moscow            |
-- | MEX        | Ciudad de México  |
-- | TUR        | Istanbul          |
-- | PAK        | Karachi           |
-- | IDN        | Jakarta           |
-- | CHN        | Shanghai          |
-- | BRA        | São Paulo         |
-- | KOR        | Seoul             |
-- | IND        | Mumbai (Bombay)   |
-- +------------+-------------------+
-- 24 rows in set (0.0017 sec)

--------------------------------------------------------------------------------------------------------------------------
-- 6. Вывести название города в Индии с самым длинным названием
select name as Город, countrycode
from city
where countrycode = 'IND'
order by char_length(name) desc
limit 1;

-- +-----------------------------------+---------------+
-- | Город                          | countrycode |
-- +-----------------------------------+---------------+
-- | Thiruvananthapuram (Trivandrum | IND         |
-- +------------------------------------+--------------+
-- 1 row in set (0.0009 sec)