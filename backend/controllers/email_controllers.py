# import smtplib
# email = 'theraidercomes1@gmail.com'
# password = input()
# smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_object.starttls()
# smtp_object.login(email, password)

# from_address = 'theraidercomes1@gmail.com'
# to_address = 'paarthbhatnagarh3h3@gmail.com'
# subject = 'Testing SMTP'
# body = 'Testing SMTP'

# message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{body}"

# smtp_object.sendmail(from_address, to_address, message)
# smtp_object.quit()
from app import celery
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from celery.schedules import crontab

@celery.on_after_finalize.connect
def setup_periodic_email_task(sender, **kwargs):
    sender.add_periodic_task(10.0, send_email_to_user.s(), name="At every 10")

@celery.task()
def send_email_to_user():
    print("THIS TASK IS BEING EXECUTED")
    # Set your SendGrid API key
    # sg_api_key = "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"
    # # Set sender, recipient, subject and message body
    # from_email = 'theraidercomes1@gmail.com'
    # to_email = 'paarthbhatnagarh3h3@gmail.com'
    # subject = 'Test email'
    # html_content = '<p>Hello World!</p>'

    # # Create the email message
    # message = Mail(
    #     from_email=from_email,
    #     to_emails=to_email,
    #     subject=subject,
    #     html_content=html_content)
    # # Initialize the SendGrid client
    # sg = SendGridAPIClient(api_key=sg_api_key)
    # # Send the email message
    # response = sg.send(message)
    print("EMAIL SENTTTT")



# Get the details for the posts for the current day from the posts table
# See how many users have posted today
# Select all the users that are not in the list of users that have posted today
# Send emails to all of them
