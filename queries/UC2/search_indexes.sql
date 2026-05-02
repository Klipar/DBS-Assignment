-- SET enable_indexscan = OFF;
-- SET enable_bitmapscan = OFF;
-- SET enable_indexonlyscan = OFF;

CREATE INDEX idx_actors_name ON actors(name);
CREATE INDEX idx_actors_surname ON actors(surname);
CREATE INDEX idx_actors_films_composite ON actors_films(actor_id, film_id);
CREATE INDEX idx_films_genres_composite ON films_genres(genre_id, film_id);
CREATE INDEX idx_films_studios_composite ON films_studios(studio_id, film_id);

-- Execution Time	3.516 ms	1.250 ms	64.5%
-- Planning Time	9.168 ms	7.350 ms	19.8%
-- Total Time	    12.684 ms	8.600 ms	32.2%