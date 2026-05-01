import psycopg2
from config import load_config


def connect():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL successfully")
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection error:", error)
        return None


if __name__ == "__main__":
    connect()