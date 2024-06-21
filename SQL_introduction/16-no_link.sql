--  lists all records of the table second_table with name from max to min score

SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;