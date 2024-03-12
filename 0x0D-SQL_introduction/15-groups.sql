-- list the number of records with the same score
-- in the table second_table or the database
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY number
ORDER BY number DESC;
