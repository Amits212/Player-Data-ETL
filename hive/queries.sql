-- Top 3 Countries by Income
SELECT c.name, SUM(p.value) AS total_income
FROM players p
JOIN countries c ON p.country_code = c.code
GROUP BY c.name
ORDER BY total_income DESC
LIMIT 3;


-- Most Valuable Clubs and Top Spending Clubs
SELECT club, MAX(value) AS max_value
FROM players
GROUP BY club;

SELECT club, SUM(salary) AS total_salary
FROM players
GROUP BY club
ORDER BY total_salary DESC
LIMIT 5;


-- Best FIFA Players by Continent
SELECT continent, AVG(fifa_score) AS avg_fifa_score
FROM players p
JOIN countries c ON p.country_code = c.code
JOIN continents co ON c.continent_code = co.code
GROUP BY continent
ORDER BY avg_fifa_score DESC;


--Section for optimization answered:
--
--Join on Indexed Columns: Join on country_code which is indexed or a foreign key.
--Aggregation: Use SUM function after converting the
--value column to a numeric format, ensuring accurate calculations.
--
--Join Operations: Join tables on indexed columns to ensure efficient data retrieval.
--Aggregation and Grouping: Use AVG function
-- and group by continent to calculate average FIFA scores.