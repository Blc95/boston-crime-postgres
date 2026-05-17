# Boston Crime PostgreSQL Database

This project builds a PostgreSQL database from a Boston crime CSV dataset.

The project includes:

- database creation
- schema creation
- basic CSV profiling
- table creation with appropriate data types
- role-based access control
- read-only and read-write users
- bulk loading with PostgreSQL `COPY`
- exploratory SQL queries

## Project Structure

```text
boston-crime-postgres/
├── data/
│   └── boston.csv
├── scripts/
│   ├── 01_create_database.py
│   ├── 02_create_schema.py
│   ├── 03_explore_data.py
│   ├── 04_create_tables.py
│   ├── 05_create_roles.py
│   ├── 06_create_users.py
│   └── 07_load_data.py
├── sql/
│   └── exploratory_queries.sql
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## Requirements

- Python 3
- PostgreSQL
- `psql` command-line tool
- `make`

Python dependencies are listed in `requirements.txt`.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```bash
cp .env.example .env
```

Then edit `.env` with your local PostgreSQL credentials:

```env
DB_NAME=crime_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

## Run the Project

Run the full database setup:

```bash
make setup
```

This will:

1. create the database
2. create the schema
3. profile the CSV file
4. create tables and custom types
5. create database roles
6. create users
7. load the CSV data into PostgreSQL

Run the exploratory SQL queries:

```bash
make queries
```

Or run everything:

```bash
make all
```

## Example Queries

The project includes exploratory SQL queries such as:

```sql
SELECT
    day_of_the_week,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY day_of_the_week
ORDER BY crime_count DESC;
```

```sql
SELECT
    description,
    COUNT(*) AS crime_count
FROM crimes.boston_crimes
GROUP BY description
ORDER BY crime_count DESC
LIMIT 10;
```

## Database Permissions

The project creates two group roles:

| Role | Permissions |
|---|---|
| `readonly` | Can connect to the database and read from tables in the `crimes` schema |
| `readwrite` | Can connect to the database and read, insert, update, and delete data in the `crimes` schema |

It also creates two example users:

| User | Role |
|---|---|
| `data_analyst` | `readonly` |
| `data_scientist` | `readwrite` |

This demonstrates basic role-based access control in PostgreSQL.

## Notes

This is a small portfolio project intended to demonstrate a practical PostgreSQL workflow. It focuses on database setup, data loading, permissions, and basic analysis rather than advanced data modeling or application development.

The `.env` file is ignored by Git and should not be committed.