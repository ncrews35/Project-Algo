from psaw import PushshiftAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime, os, smtplib
import config, contact_list, queries
import algo
import alpaca_trade_api as tradeapi
import psycopg2, psycopg2.extras

def send_mail():
    # Specify paper trading environment
    os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

    account = queries.get_account

    contacts = contact_list.contacts
    
    # The mail addresses and password
    sender_address = config.email
    sender_pass = config.password

    # The logic of the algorithm
    mail_content = algo.run_logic()

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

    