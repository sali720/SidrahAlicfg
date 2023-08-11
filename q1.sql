USE foundation_assessment_ii;

UPDATE showings AS s1
JOIN (
    SELECT movie_ID, MAX(start_time) AS max_start_time
    FROM showings
    WHERE movie_ID = 2
    GROUP BY movie_ID
) AS s2 ON s1.movie_ID = s2.movie_ID AND s1.start_time = s2.max_start_time
SET s1.available_seats = 0;
