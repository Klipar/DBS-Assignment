import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(67)

NUM_STAFF = 30
NUM_HALLS = 8
NUM_FILMS = 200
NUM_ACTORS = 200
NUM_GENRES = 15
NUM_STUDIOS = 20
NUM_SCREENINGS = 1000
NUM_SALES = 10000

def generate_seed():
    with open('seed.sql', 'w', encoding='utf-8') as f:
        # Clearing old data before a new seed
        f.write("TRUNCATE TABLE sales, shifts_screenings, actors_films, films_genres, films_studios, shifts, screenings, staffs, halls, films, actors, genres, studios RESTART IDENTITY CASCADE;\n\n")

        # 1. STAFFS
        f.write("-- Staffs\n")
        positions = ['Manager', 'Cashier', 'Cleaner', 'Technician', 'Security']
        for i in range(1, NUM_STAFF + 1):
            name = fake.first_name()
            surname = fake.last_name()
            age = random.randint(18, 60)
            pos = random.choice(positions)
            date = fake.date_between(start_date = '-2y', end_date = 'today')
            f.write(f"INSERT INTO staffs (name, surname, age, position, working_since) VALUES ('{name}', '{surname}', {age}, '{pos}', '{date}');\n")

        # 2. HALLS
        f.write("\n-- Halls\n")
        for i in range(1, NUM_HALLS + 1):
            name = f"Hall {i}"
            capacity = random.choice([30, 50, 100, 150])
            f.write(f"INSERT INTO halls (name, capacity) VALUES ('{name}', {capacity});\n")

        # 3. FILMS
        f.write("\n-- Films\n")
        age_groups = ['G', 'PG', 'PG-13', 'R', 'NC-17']
        for i in range(1, NUM_FILMS + 1):
            name = fake.sentence(nb_words = 3).replace('.', '')
            duration = random.randint(80, 180)
            age_group = random.choice(age_groups)
            f.write(f"INSERT INTO films (name, duration, age_group) VALUES ('{name}', {duration}, '{age_group}');\n")

        # 4. ACTORS, GENRES, STUDIOS
        f.write("\n-- Actors, Genres, Studios\n")
        for i in range(1, NUM_ACTORS + 1):
            f.write(f"INSERT INTO actors (name, surname) VALUES ('{fake.first_name()}', '{fake.last_name()}');\n")

        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Documentary', 'Thriller', 'Animation', 'Crime', 'Fantasy']
        for name in genres:
            f.write(f"INSERT INTO genres (name) VALUES ('{name}');\n")

        for i in range(1, NUM_STUDIOS + 1):
            f.write(f"INSERT INTO studios (name) VALUES ('{fake.company()} Studio');\n")

        # 5. SCREENINGS
        f.write("\n-- Screenings\n")
        languages = ['EN', 'UA', 'SK']
        screening_ids = []
        for i in range(1, NUM_SCREENINGS + 1):
            start_time = fake.date_time_between(start_date = '-1y', end_date = '+1m')
            lang = random.choice(languages)
            film_id = random.randint(1, NUM_FILMS)
            hall_id = random.randint(1, NUM_HALLS)
            f.write(f"INSERT INTO screenings (start_time, language, film_id, hall_id) VALUES ('{start_time}', '{lang}', {film_id}, {hall_id});\n")
            screening_ids.append(i)

        # 6. SALES
        f.write("\n-- Sales\n")
        for i in range(1, NUM_SALES + 1):
            c_name = fake.first_name()
            c_surname = fake.last_name()
            c_age = random.randint(10, 70)
            scr_id = random.choice(screening_ids)
            f.write(f"INSERT INTO sales (customer_name, customer_surname, customer_age, screening_id) VALUES ('{c_name}', '{c_surname}', {c_age}, {scr_id});\n")

        # 7. SHIFTS
        f.write("\n-- Shifts\n")
        for i in range(1, (NUM_STAFF * 10) + 1):
            start = fake.date_time_between(start_date = '-1y', end_date = 'now')
            end = start + timedelta(hours = 8)
            staff_id = random.randint(1, NUM_STAFF)
            f.write(f"INSERT INTO shifts (description, start_time, end_time, staff_id) VALUES ('Regular shift', '{start}', '{end}', {staff_id});\n")

        # 8. JUNCTION TABLES (Actors_Films, Films_Genres, etc.)
        f.write("\n-- Junction Tables\n")

        for film_id in range(1, NUM_FILMS + 1):
            # 8.1. Actors <-> Films
            for _ in range(random.randint(2, 4)):
                f.write(f"INSERT INTO actors_films (actor_id, film_id) VALUES ({random.randint(1, NUM_ACTORS)}, {film_id});\n")

            # 8.2. Films <-> Genres
            for _ in range(random.randint(1, 2)):
                f.write(f"INSERT INTO films_genres (film_id, genre_id) VALUES ({film_id}, {random.randint(1, len(genres))});\n")

            # 8.3. Films <-> Studios
            for _ in range(random.randint(1, 2)):
                f.write(f"INSERT INTO films_studios (film_id, studio_id) VALUES ({film_id}, {random.randint(1, NUM_STUDIOS)});\n")

        # 8.4. Shifts <-> Screenings
        for shift_id in range(1, (NUM_STAFF * 10) + 1):
            for _ in range(random.randint(3, 6)):
                f.write(f"INSERT INTO shifts_screenings (shift_id, screening_id) VALUES ({shift_id}, {random.randint(1, NUM_SCREENINGS)});\n")

    print(f"seed.sql generated.")

if __name__ == "__main__":
    generate_seed()
