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
        f.write("TRUNCATE TABLE sales, shifts_screenings, actors_films, films_genres, films_studios, shifts, screenings, staffs, halls, films, actors, genres, studios RESTART IDENTITY CASCADE;\n\n")

        # 1. STAFFS
        f.write("-- Staffs\n")
        positions = ['Manager', 'Cashier', 'Cleaner', 'Technician', 'Security']
        for i in range(1, NUM_STAFF + 1):
            name = fake.first_name()[:31]
            surname = fake.last_name()[:31]
            f.write(f"INSERT INTO staffs (name, surname, age, position, working_since) VALUES ('{name}', '{surname}', {random.randint(15, 60)}, '{random.choice(positions)}', '{fake.date_between(start_date = '-2y', end_date = 'today')}');\n")

        # 2. HALLS
        f.write("\n-- Halls\n")
        for i in range(1, NUM_HALLS + 1):
            f.write(f"INSERT INTO halls (name, capacity) VALUES ('Hall {i}', {random.choice([30, 50, 100, 150])});\n")

        # 3. FILMS
        f.write("\n-- Films\n")
        age_groups = ['G', 'PG', 'PG-13', 'R', 'NC-17']
        for i in range(1, NUM_FILMS + 1):
            name = fake.sentence(nb_words = 3).replace('.', '')[:31]
            f.write(f"INSERT INTO films (name, duration, age_group) VALUES ('{name}', {random.randint(80, 180)}, '{random.choice(age_groups)}');\n")

        # 4. ACTORS
        f.write("\n-- Actors\n")
        for i in range(1, NUM_ACTORS + 1):
            f.write(f"INSERT INTO actors (name, surname) VALUES ('{fake.first_name()[:31]}', '{fake.last_name()[:31]}');\n")

        # 5. GENRES
        f.write("\n-- Genres\n")
        genres_list = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Documentary', 'Thriller', 'Animation', 'Crime', 'Fantasy', 'Musical', 'Western', 'History', 'Adventure', 'Noir']
        for name in genres_list:
            f.write(f"INSERT INTO genres (name) VALUES ('{name[:31]}');\n")

        # 6. STUDIOS
        f.write("\n-- Studios\n")
        used_studios = set()
        while len(used_studios) < NUM_STUDIOS:
            s_name = fake.company()[:24] + " Studio"
            if s_name not in used_studios:
                f.write(f"INSERT INTO studios (name) VALUES ('{s_name}');\n")
                used_studios.add(s_name)

        # 7. SCREENINGS
        f.write("\n-- Screenings\n")
        languages = ['EN', 'UA', 'SK']
        for i in range(1, NUM_SCREENINGS + 1):
            f.write(f"INSERT INTO screenings (start_time, language, film_id, hall_id) VALUES ('{fake.date_time_between(start_date = '-1y', end_date = '+1m')}', '{random.choice(languages)}', {random.randint(1, NUM_FILMS)}, {random.randint(1, NUM_HALLS)});\n")

        # 8. SALES
        f.write("\n-- Sales\n")
        for i in range(1, NUM_SALES + 1):
            f.write(f"INSERT INTO sales (customer_name, customer_surname, customer_age, screening_id) VALUES ('{fake.first_name()[:31]}', '{fake.last_name()[:31]}', {random.randint(10, 70)}, {random.randint(1, NUM_SCREENINGS)});\n")

        # 9. SHIFTS
        f.write("\n-- Shifts\n")
        total_shifts = NUM_STAFF * 10
        for i in range(1, total_shifts + 1):
            start = fake.date_time_between(start_date = '-1y', end_date = 'now')
            f.write(f"INSERT INTO shifts (description, start_time, end_time, staff_id) VALUES ('Regular shift', '{start}', '{start + timedelta(hours = 8)}', {random.randint(1, NUM_STAFF)});\n")

        # 10. JUNCTION TABLES
        f.write("\n-- Junction Tables\n")
        for film_id in range(1, NUM_FILMS + 1):
            for _ in range(random.randint(2, 4)):
                f.write(f"INSERT INTO actors_films (actor_id, film_id) VALUES ({random.randint(1, NUM_ACTORS)}, {film_id});\n")
            for _ in range(random.randint(1, 2)):
                f.write(f"INSERT INTO films_genres (film_id, genre_id) VALUES ({film_id}, {random.randint(1, len(genres_list))});\n")
            for _ in range(random.randint(1, 2)):
                f.write(f"INSERT INTO films_studios (film_id, studio_id) VALUES ({film_id}, {random.randint(1, NUM_STUDIOS)});\n")

        for shift_id in range(1, total_shifts + 1):
            for _ in range(random.randint(3, 6)):
                f.write(f"INSERT INTO shifts_screenings (shift_id, screening_id) VALUES ({shift_id}, {random.randint(1, NUM_SCREENINGS)});\n")

    print(f"DONE! seed.sql generated.")

if __name__ == "__main__":
    generate_seed()
