-- lists No. of rows with the same score
SELECT score, COUNT(*) AS `number`
FROM second_table
GROUP BY score;
