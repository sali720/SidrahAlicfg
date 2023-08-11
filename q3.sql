USE foundation_assessment_ii;

SELECT DISTINCT mi.movie_name
FROM movie_info mi
INNER JOIN showings s ON mi.movie_ID = s.movie_ID
LEFT JOIN screens sc ON s.screen_ID = sc.screen_ID AND sc.four_k = True
WHERE sc.screen_ID IS NULL;
