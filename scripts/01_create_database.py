import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = "crime_db"

conn = psycopg2.connect(
    dbname="postgres",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
)
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute(
        """
        SELECT 1
        FROM pg_database
        WHERE datname = %s;
        """,
        (DB_NAME,)
    )

    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")

conn.close()