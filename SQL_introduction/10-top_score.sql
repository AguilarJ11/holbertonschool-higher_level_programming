-- list rows in second_table only display name and score, from max score to min

SELECT score, name
FROM second_table
ORDER BY score DESC;
