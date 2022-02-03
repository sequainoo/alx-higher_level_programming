-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- Load into db
-- Displays Max temperature of each state ordered by state name
SELECT state, MAX(`value`) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
