-- Count crimes by weekday
SELECT
    day_of_the_week,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY day_of_the_week
ORDER BY crime_count DESC;


-- Top 10 most common crime descriptions
SELECT
    description,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY description
ORDER BY crime_count DESC
LIMIT 10;


-- Count crimes by date
SELECT
    incident_date,
    COUNT(*) AS daily_crimes
FROM crimes.boston_crimes
GROUP BY incident_date
ORDER BY incident_date;


-- Count crimes by offense code
SELECT
    offense_code,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY offense_code
ORDER BY crime_count DESC
LIMIT 10;


-- Find crimes with missing coordinates
SELECT
    COUNT(*) AS missing_coordinate_count
FROM crimes.boston_crimes
WHERE lat IS NULL
   OR lon IS NULL;


-- Crimes by weekday and description
SELECT
    day_of_the_week,
    description,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY
    day_of_the_week,
    description
ORDER BY crime_count DESC
LIMIT 20;