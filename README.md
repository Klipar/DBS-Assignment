# Cinema Database

Implementation of a cinema management system with automated data initialization.

## Structure
* `schema.sql` – DDL (Tables and constraints).
* `seed.sql` – 14,000+ records (Fixed seed).
* `seed.py` – Python script for data generation.
* `docker-compose.yml` – Database environment.

## Usage

1. **Start:**
   ```bash
   docker compose up -d
   ```
   On first start, PostgreSQL automatically executes files from `./docker-entrypoint-initdb.d/` in alphabetical order (`schema.sql` first, then `seed.sql`).

2. **Reset:**
   To re-initialize the database from scratch:
   ```bash
   docker compose down -v
   docker compose up -d
   ```

## Reproducibility
The `seed.sql` file is deterministic (uses `Faker.seed(67)`).
To regenerate:
```bash
pip install Faker
python seed.py
```
