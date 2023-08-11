USE foundation_assessment_ii;

SELECT mi.movie_name, s.start_time,
       ADDTIME(s.start_time, mi.movie_length) AS end_time
FROM movie_info mi
JOIN showings s ON mi.movie_ID = s.movie_ID;
