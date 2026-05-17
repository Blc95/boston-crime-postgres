setup:
	python scripts/01_create_database.py
	python scripts/02_create_schema.py
	python scripts/03_explore_data.py
	python scripts/04_create_tables.py
	python scripts/05_create_roles.py
	python scripts/06_create_users.py
	python scripts/07_load_data.py

queries:
	psql -d crime_db -f sql/exploratory_queries.sql

all: setup queries