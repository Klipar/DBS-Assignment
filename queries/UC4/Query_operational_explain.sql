-- Parameters:
--   $1 = film_id of the new screening
--   $2 = hall_id of the new screening
--   $3 = start_time (timestamp) of the new screening
--   $4 = language of the new screening

EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
INSERT INTO screenings (film_id, hall_id, start_time, language)
VALUES ($1, $2, $3, $4);

-- idx execution time: 0.4 ms
-- no idx execution time: 0.1 ms