import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM pg_type
                    WHERE typname = 'day_of_the_week'
                ) THEN
                    CREATE TYPE day_of_the_week AS ENUM (
                        'Monday',
                        'Tuesday',
                        'Wednesday',
                        'Thursday',
                        'Friday',
                        'Saturday',
                        'Sunday'
                    );
                END IF;
            END
            $$;
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS crimes.boston_crimes (
                incident_number int4 PRIMARY KEY,
                offense_code int4,
                description varchar(100),
                date date,
                day_of_the_week day_of_the_week,
                lat float,
                lon float
            );
            """
        )