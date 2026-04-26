# Cinema System — Seeding & Reproducibility

This project implements the physical database model for a cinema management system with a fully reproducible data seeding process.

## Project Structure
* `schema.sql` — Database structure (DDL).
* `seed.py` — Data generator script (Python).
* `seed.sql` — Generated dataset (14,000+ records).
* `docker-compose.yml` — PostgreSQL environment configuration.

## Setup Instructions

1. **Start the Database:**
   ```bash
   docker compose up -d
   ```

2. **Initialize the Schema:**
   ```bash
   docker exec -i cinema_db psql -U postgres -d cinema_db < schema.sql
   ```

3. **Populate Data:**
   ```bash
   docker exec -i cinema_db psql -U postgres -d cinema_db < seed.sql
   ```

## Reproducibility
The `seed.sql` file is generated via `seed.py`. To ensure the dataset remains identical across all environments, a fixed seed is used:
```python
Faker.seed(67)
```
To re-generate the file:
1. Install dependency: `pip install Faker`.
2. Run: `python seed.py`.
