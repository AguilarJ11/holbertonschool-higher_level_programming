-- lists all the cities of California that can be found in the database hbtn_0d_usa

USE hbtn_0d_usa
SET @state_california = (SELECT id FROM states WHERE name = 'California');
SELECT *
FROM *
WHERE state_id = @state_california
ORDER BY id ASC;