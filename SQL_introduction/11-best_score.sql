-- list rows in second_table only display name and score > 10, from max score to min

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;