
/*
This file will display the commands used to download the CSV files
from the online database using SQL.

It should be noted that because my city could not be found in the
city_list, I have downloaded the information for "Berlin" instead.
*/

-- Proof that Bonn is not in city_list
SELECT *
FROM city_list
where country = 'Germany';
-- Returns three cities, Berlin, Hamburg and Munch but not Bonn or Cologne.

-- Download the temperature data for Berlin
SELECT *
FROM city_data
WHERE city = 'Berlin';
-- Saved as 'BerlinYearlyAvgTemp.csv'

--Download global temperature data
Select *
FROM global_data;
-- Saved as 'GlobalYearlyAvgTemp.csv'

-- SQL query complete!
