CREATE INDEX idx_screenings_hall_start_film
ON screenings (hall_id, start_time, film_id);

DROP INDEX IF EXISTS idx_screenings_hall_start_film;