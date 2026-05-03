-- 1. ENUM TYPES

CREATE TYPE staff_position AS ENUM ('Manager', 'Cashier', 'Cleaner', 'Technician', 'Security');
CREATE TYPE screening_language AS ENUM ('EN', 'UA', 'SK');
CREATE TYPE film_age_group AS ENUM ('G', 'PG', 'PG-13', 'R', 'NC-17');


-- 2. TABLES WITHOUT FOREIGN KEYS

-- staffs table
CREATE TABLE staffs (
                        id SMALLSERIAL PRIMARY KEY,
                        name VARCHAR(32) NOT NULL,
                        surname VARCHAR(32) NOT NULL,
                        age SMALLINT CHECK (age >= 15),
                        position staff_position NOT NULL,
                        working_since DATE DEFAULT CURRENT_DATE
);

-- halls table
CREATE TABLE halls (
                       id SMALLSERIAL PRIMARY KEY,
                       name VARCHAR(16) UNIQUE NOT NULL,
                       capacity SMALLINT NOT NULL CHECK (capacity > 0)
);

-- films table
CREATE TABLE films (
                       id SMALLSERIAL PRIMARY KEY,
                       name VARCHAR(256) NOT NULL,
                       duration SMALLINT NOT NULL CHECK (duration > 0),
                       age_group film_age_group NOT NULL
);

-- actors table
CREATE TABLE actors (
                        id SMALLSERIAL PRIMARY KEY,
                        name VARCHAR(32) NOT NULL,
                        surname VARCHAR(32) NOT NULL
);

-- genres table
CREATE TABLE genres (
                        id SMALLSERIAL PRIMARY KEY,
                        name VARCHAR(32) UNIQUE NOT NULL
);

-- studios table
CREATE TABLE studios (
                         id SMALLSERIAL PRIMARY KEY,
                         name VARCHAR(32) UNIQUE NOT NULL
);


-- 3. TABLES WITH FOREIGN KEYS

-- shifts table
CREATE TABLE shifts (
                        id SMALLSERIAL PRIMARY KEY,
                        description VARCHAR(512),
                        start_time TIMESTAMP NOT NULL,
                        end_time TIMESTAMP NOT NULL CHECK (end_time > start_time),
                        staff_id SMALLINT NOT NULL REFERENCES staffs(id)
                            ON DELETE RESTRICT
                            ON UPDATE CASCADE
);

-- screenings table
CREATE TABLE screenings (
                            id SMALLSERIAL PRIMARY KEY,
                            start_time TIMESTAMP NOT NULL,
                            language screening_language NOT NULL,
                            film_id SMALLINT NOT NULL REFERENCES films(id)
                                ON DELETE RESTRICT
                                ON UPDATE CASCADE,
                            hall_id SMALLINT NOT NULL REFERENCES halls(id)
                                ON DELETE RESTRICT
                                ON UPDATE CASCADE
);

-- sales table
CREATE TABLE sales (
                       id SMALLSERIAL PRIMARY KEY,
                       customer_name VARCHAR(32) NOT NULL,
                       customer_surname VARCHAR(32) NOT NULL,
                       customer_age SMALLINT CHECK (customer_age >= 0),
                       screening_id SMALLINT NOT NULL REFERENCES screenings(id)
                           ON DELETE RESTRICT
                           ON UPDATE CASCADE
);

-- shifts_screenings
CREATE TABLE shifts_screenings (
                                   id SMALLSERIAL PRIMARY KEY,
                                   shift_id SMALLINT NOT NULL REFERENCES shifts(id)
                                       ON DELETE RESTRICT
                                       ON UPDATE CASCADE,
                                   screening_id SMALLINT NOT NULL REFERENCES screenings(id)
                                       ON DELETE RESTRICT
                                       ON UPDATE CASCADE
);

-- actors_films
CREATE TABLE actors_films (
                              id SMALLSERIAL PRIMARY KEY,
                              actor_id SMALLINT NOT NULL REFERENCES actors(id)
                                  ON DELETE RESTRICT
                                  ON UPDATE CASCADE,
                              film_id SMALLINT NOT NULL REFERENCES films(id)
                                  ON DELETE RESTRICT
                                  ON UPDATE CASCADE
);

-- films_genres
CREATE TABLE films_genres (
                              id SMALLSERIAL PRIMARY KEY,
                              film_id SMALLINT NOT NULL REFERENCES films(id)
                                  ON DELETE RESTRICT
                                  ON UPDATE CASCADE,
                              genre_id SMALLINT NOT NULL REFERENCES genres(id)
                                  ON DELETE RESTRICT
                                  ON UPDATE CASCADE
);

-- films_studios
CREATE TABLE films_studios (
                               id SMALLSERIAL PRIMARY KEY,
                               film_id SMALLINT NOT NULL REFERENCES films(id)
                                   ON DELETE RESTRICT
                                   ON UPDATE CASCADE,
                               studio_id SMALLINT NOT NULL REFERENCES studios(id)
                                   ON DELETE RESTRICT
                                   ON UPDATE CASCADE
);


-- 3. INDEXES

DROP INDEX IF EXISTS idx_actors_name;
DROP INDEX IF EXISTS idx_actors_surname;
DROP INDEX IF EXISTS idx_actors_films_composite;
DROP INDEX IF EXISTS idx_films_genres_composite;
DROP INDEX IF EXISTS idx_films_studios_composite;

DROP INDEX IF EXISTS idx_screenings_film_start;
DROP INDEX IF EXISTS idx_sales_screening_id;

DROP INDEX IF EXISTS idx_screenings_hall_start_film;


CREATE INDEX idx_actors_name ON actors(name);
CREATE INDEX idx_actors_surname ON actors(surname);
CREATE INDEX idx_actors_films_composite ON actors_films(actor_id, film_id);
CREATE INDEX idx_films_genres_composite ON films_genres(genre_id, film_id);
CREATE INDEX idx_films_studios_composite ON films_studios(studio_id, film_id);

CREATE INDEX idx_screenings_film_start ON screenings(film_id, start_time);
CREATE INDEX idx_sales_screening_id ON sales(screening_id);

CREATE INDEX idx_screenings_hall_start_film ON screenings (hall_id, start_time, film_id);
