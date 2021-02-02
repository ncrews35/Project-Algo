#  Where the magic happens
from psaw import PushshiftAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime, os, smtplib
import config, contact_list, queries
import alpaca_trade_api as tradeapi
import psycopg2, psycopg2.extras



def avenueb_trading_algo():
    # Specify paper trading environment
    os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

    account = queries.get_account

    contacts = contact_list.contacts
    
    # The mail addresses and password
    sender_address = config.email
    sender_pass = config.password

    # The logic of the algorithm
    mail_content = run_logic()

    # Setup MIME
    message = MIMEMultipart()
    message['From'] = 'Avenue B Algo'
    message['Subject'] = 'Daily Algo Report'  # The subject line

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security

    # login with mail_id and password
    session.login(sender_address, sender_pass)

    for contact in contacts:
        message['To'] = contact
        text = message.as_string()
        session.sendmail(sender_address, contact, text)

    session.quit()

    done = 'Mail Sent'

    return done


def run_logic():
    mc = queries.get_mention_counts()
    count = 0 
    temp = []
    for m in mc:
        temp.append(m)
        count += 1
        if count > 9:
            break
    
    str1 = ""
    for t in temp:
        str1 += str(t)

    hml = "<!DOCTYPE html><html><head></head><body><h1>Your Daily Algo Report</h1><h3>Today's Picks</h3><p>" + str1 + "</p><br><P>Best,</P><p>Avenue B Algo</P></body></html>"
    
    return hml


avenueb_trading_algo()