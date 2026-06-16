-- Query 1: Top Countries

SELECT country,
       COUNT(*) AS total_titles
FROM netflix
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- Query 2: Movies vs TV Shows

SELECT type,
       COUNT(*) AS total_content
FROM netflix
GROUP BY type;

-- Query 3: Rating Distribution

SELECT rating,
       COUNT(*) AS total_titles
FROM netflix
GROUP BY rating
ORDER BY total_titles DESC;

-- Query 4: Release Year Analysis

SELECT release_year,
       COUNT(*) AS total_titles
FROM netflix
GROUP BY release_year
ORDER BY total_titles DESC;

-- Query 5: Top Directors

SELECT director,
       COUNT(*) AS total_titles
FROM netflix
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;

-- Query 6: Countries Producing Movies

SELECT country,
       COUNT(*) AS total_titles
FROM netflix
WHERE type='Movie'
GROUP BY country
ORDER BY total_titles DESC;

-- Query 7: TV Show Ratings

SELECT rating,
       COUNT(*) AS total_titles
FROM netflix
WHERE type='TV Show'
GROUP BY rating
ORDER BY total_titles DESC;