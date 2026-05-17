import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "data" / "boston.csv"

load_dotenv()

with psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
) as conn:
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE crimes.boston_crimes;")

        with open(CSV_PATH) as f:
            cur.copy_expert(
                """
                COPY crimes.boston_crimes
                FROM STDIN
                WITH CSV HEADER;
                """,
                f
            )