import smtplib
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
# from app import celery

# @celery.task
# def send_email_to_user():
print("THIS TASK IS BEING EXECUTED")
email = 'theraidercomes1@gmail.com'
password = 'qxmpjjqtskwbxyow'
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login(email, password)

from_address = 'theraidercomes1@gmail.com'
to_address = 'paarthbhatnagarh3h3@gmail.com'
subject = 'Testing SMTP 2'
body = 'Testing SMTP 2'

message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{body}"

smtp_object.sendmail(from_address, to_address, message)
smtp_object.quit()


# Get the details for the posts for the current day from the posts table
# See how many users have posted today
# Select all the users that are not in the list of users that have posted today
# Send emails to all of them
