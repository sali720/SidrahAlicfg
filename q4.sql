USE foundation_assessment_ii;

SELECT mi.movie_name, s.start_time
FROM movie_info mi
JOIN showings s ON mi.movie_ID = s.movie_ID
ORDER BY s.available_seats DESC
LIMIT 1;
