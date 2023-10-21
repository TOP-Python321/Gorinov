insert into styles 
    (style)
values 
    ('pop'),
    ('rok');
    
insert into singers 
    (singer)
values 
    ('The Beatles'),
    ('Queen');

insert into publishers 
    (publisher, country)
values 
    ('Parlophone', 'United Kingdom');
    
insert into collections 
    (name, date, styles_id, publishers_id)
values 
    ('Queen', '1981-12-01', 2, 1);
 
insert into songs 
    (song, styles_id, singers_id)
values 
    ('Queen_song', 2, 2); 
    
insert into collections_songs 
    (collections_id, songs_id)
values 
    (1, 1); 
  
insert into collections_singers 
    (collections_id, singers_id)
values 
    (1, 2);
    

-- +-----------------------+
-- | Tables_in_mus_library |
-- +-----------------------+
-- | collections           |
-- | collections_singers   |
-- | collections_songs     |
-- | publishers            |
-- | singers               |
-- | songs                 |
-- | styles                |
-- +-----------------------+
-- 7 rows in set (0.0015 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from styles;
-- +----+-------+
-- | id | style |
-- +----+-------+
-- |  1 | pop   |
-- |  2 | rok   |
-- +----+-------+
-- 2 rows in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from songs;
-- +----+------------+-----------+------------+
-- | id | song       | styles_id | singers_id |
-- +----+------------+-----------+------------+
-- |  1 | Queen_song |         2 |          2 |
-- +----+------------+-----------+------------+
-- 1 row in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from singers;
-- +----+-------------+
-- | id | singer      |
-- +----+-------------+
-- |  2 | Queen       |
-- |  1 | The Beatles |
-- +----+-------------+
-- 2 rows in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from publishers;
-- +----+------------+----------------+
-- | id | publisher  | country        |
-- +----+------------+----------------+
-- |  1 | Parlophone | United Kingdom |
-- +----+------------+----------------+
-- 1 row in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from collections_songs;
-- +----------------+----------+
-- | collections_id | songs_id |
-- +----------------+----------+
-- |              1 |        1 |
-- +----------------+----------+
-- 1 row in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from collections_singers;
-- +----------------+------------+
-- | collections_id | singers_id |
-- +----------------+------------+
-- |              1 |          2 |
-- +----------------+------------+
-- 1 row in set (0.0005 sec)
 -- MySQL  localhost:3306 ssl  mus_library  SQL > select * from collections;
-- +----+-------+------------+-----------+---------------+
-- | id | name  | date       | styles_id | publishers_id |
-- +----+-------+------------+-----------+---------------+
-- |  1 | Queen | 1981-12-01 |         2 |             1 |
-- +----+-------+------------+-----------+---------------+
-- 1 row in set (0.0005 sec)