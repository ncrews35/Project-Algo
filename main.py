from psaw import PushshiftAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime, os, smtplib, algo, mailer
import config, contact_list, queries, reset, search_reddit
import alpaca_trade_api as tradeapi
import psycopg2, psycopg2.extras

def main (data,context):
    # os.environ(["PATH]"] + os.pathsep + "/usr/local/bin")
    reset.reset_mentions()
    search_reddit.get_reddit_data()
    mailer.send_mail()
    

if __name__ == "__main__":
    main('data','context')
