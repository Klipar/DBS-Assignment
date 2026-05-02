-- Check conflicts before inserting a new screening
-- Parameters:
--   $1 = film_id of the new screening
--   $2 = hall_id of the new screening
--   $3 = start_time (timestamp) of the new screening
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT COUNT(*) AS overlapping_screenings
FROM screenings s
JOIN films existing_film ON existing_film.id = s.film_id
JOIN films new_film ON new_film.id = $1
WHERE s.hall_id = $2
AND (($3::timestamptz), ($3::timestamptz + make_interval(mins => new_film.duration)))
OVERLAPS
(s.start_time, s.start_time + make_interval(mins => existing_film.duration));

-- All hit no idx execution time: 0.170 ms
-- All hit idx execution time: 0.156 ms