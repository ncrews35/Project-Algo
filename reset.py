from psaw import PushshiftAPI
import datetime
import config
import psycopg2
import psycopg2.extras

def reset_mentions():
    connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("""
        DELETE FROM mention;
    """)

    connection.commit()


