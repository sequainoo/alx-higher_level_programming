-- lists all records of second_table of hbnt_0c_0
-- doesnt list rows without a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
