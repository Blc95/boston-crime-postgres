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
                    SELECT 1 FROM pg_roles WHERE rolname = 'readonly'
                ) THEN
                    CREATE ROLE readonly NOLOGIN;
                END IF;

                IF NOT EXISTS (
                    SELECT 1 FROM pg_roles WHERE rolname = 'readwrite'
                ) THEN
                    CREATE ROLE readwrite NOLOGIN;
                END IF;
            END
            $$;

            REVOKE ALL 
            ON SCHEMA public
            FROM PUBLIC;

            REVOKE ALL
            ON DATABASE crime_db
            FROM PUBLIC;

            GRANT CONNECT 
            ON DATABASE crime_db 
            TO readonly, readwrite;

            GRANT USAGE 
            ON SCHEMA crimes
            TO readonly, readwrite;

            GRANT SELECT 
            ON ALL TABLES IN SCHEMA crimes
            TO readonly;

            GRANT SELECT, INSERT, UPDATE, DELETE
            ON ALL TABLES IN SCHEMA crimes
            TO readwrite;

            ALTER DEFAULT PRIVILEGES IN SCHEMA crimes
            GRANT SELECT 
            ON TABLES 
            TO readonly;

            ALTER DEFAULT PRIVILEGES IN SCHEMA crimes
            GRANT SELECT, INSERT, UPDATE, DELETE
            ON TABLES 
            TO readwrite;
            """
        )