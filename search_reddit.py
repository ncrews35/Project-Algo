from psaw import PushshiftAPI
import datetime
from datetime import timedelta
import config
import psycopg2
import psycopg2.extras

def get_reddit_data():
    connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("""
        SELECT * FROM stock
    """)

    rows = cursor.fetchall()

    print(rows)

    stocks = {}
    for row in rows:
        stocks['$' + row['symbol']] = row['id']

    api = PushshiftAPI()

    ys = datetime.datetime.now() - timedelta(1)
    start_epoch = int(datetime.datetime(ys.year, ys.month, ys.day).timestamp())

    submissions = list(api.search_submissions(after=start_epoch,
                                        subreddit='wallstreetbets',
                                        filter=['url','author', 'title', 'subreddit']))

    for submission in submissions:

        words = submission.title.split()
        cashtags = list(set(filter(lambda word: word.lower().startswith('$'), word.isUpper(), word., words)))

        if len(cashtags) > 0:
            print(cashtags)
            print(submission.title)
            
            for cashtag in cashtags:
                if cashtag in stocks:
                    submitted_time = datetime.datetime.fromtimestamp(submission.created_utc).isoformat()

                    try:
                        cursor.execute("""
                            INSERT INTO mention (dt, stock_id, message, source, url)
                            VALUES (%s, %s, %s, 'wallstreetbets', %s)
                        """, (submitted_time, stocks[cashtag], submission.title, submission.url))

                        connection.commit()
                    except Exception as err:
                        print(err)
                        connection.rollback()



def just_GME():
    connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


    api = PushshiftAPI()

    ys = datetime.datetime.now() - timedelta(1)
    start_epoch = int(datetime.datetime(ys.year, ys.month, ys.day).timestamp())

    submissions = api.search_submissions(after=start_epoch,
                                        subreddit='wallstreetbets',
                                        filter=['url','author', 'title', 'subreddit'])

    for submission in submissions:

        words = submission.title.split()
        cashtags = list(set(filter(lambda word: word.lower().startswith("gme"), words)))
        # print(cashtags)

        if len(cashtags) > 0:
            print(cashtags)
            print(submission.title)
            for cashtag in cashtags:
                submitted_time = datetime.datetime.fromtimestamp(submission.created_utc).isoformat()
                try:
                    cursor.execute("""
                        INSERT INTO individual_stocks (dt, message, source, url)
                        VALUES (%s, %s, 'wallstreetbets', %s)
                    """, (submitted_time, cashtag, submission.title, submission.url))

                    connection.commit()
                except Exception as err:
                    print(err)
                    connection.rollback()

# just_GME()