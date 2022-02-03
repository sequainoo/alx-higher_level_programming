-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- Load into db
-- Displays the avg temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city` , AVG(`value`) AS avg_temp
FROM temperature
GROUP BY `city`
ORDER BY avg_temp DESC;
