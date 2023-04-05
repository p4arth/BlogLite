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
import requests
from flask import request
from flask import make_response
from flask_cors import cross_origin
from app import celery, users_logged_in_today
from app import app, token_required, cache
import os
import pandas as pd
from io import StringIO
import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from celery.schedules import crontab
from models.models import User, db, Post, Followers
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import datetime
from flask import render_template

# @celery.on_after_finalize.connect
# def setup_periodic_email_task(sender, **kwargs):
#     sender.add_periodic_task(10.0, send_email_to_user.s(), name="At every 10")

# schedule = crontab(day_of_month='1', hour='0', minute='0')
# schedule = crontab(second='10')
# @celery.on_after_finalize.connect
# def setup_periodic_email_task(sender, **kwargs):
#     sender.add_periodic_task(
#         30.0,
#         send_month_report_to_users.s(),
#         name='monthly_report'
#     )

def get_usernames_posted_today():
    dt = datetime.datetime.now().strftime('%d/%m/%Y') + "%"
    today_posts = db.session.query(Post).filter(Post.timestamp.not_like(dt)).all()
    return today_posts

@celery.task()
def send_email_to_user():
    print("THIS TASK IS BEING EXECUTED")
    posts = get_usernames_posted_today()
    print("--------------------------------------------------------------")
    print(posts)
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
    # 
    # print(users_logged_in_today)
    # print("EMAIL SENTTTT")


def in_current_month(timestamp):
    dt = datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')
    current_month = datetime.datetime.now().month
    return dt.month == current_month

def generate_monthly_report(username):
    user_posts_info = db.session.query(Post).filter(Post.username == username).all()
    followers_info = db.session.query(Followers).filter(Followers.follows == username).all()
    total_posts = len(user_posts_info)
    total_followers = len(followers_info)
    posts_this_month = 0
    for post in user_posts_info:
        if in_current_month(post.timestamp):
            posts_this_month = posts_this_month + 1
    return {
        "total_posts": total_posts,
        "total_followers": total_followers,
        "posts_this_month": posts_this_month
    }

@celery.task
def send_month_report_to_users():
    print("SENDING EMAILLL")
    all_user_info = db.session.query(User).all()
    for user in all_user_info:
        report = generate_monthly_report(user.username)
        report_html_string = render_template('report.html', report = report)
        message = Mail(
            from_email = 'theraidercomes1@gmail.com',
            to_emails = user.email,
            subject = 'Monthly Engagement Report',
            html_content = report_html_string,
        )
        try:
            sg = SendGridAPIClient(api_key="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")
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
    print("EMAIL SENTTT")

@celery.task
def export_blog_to_csv_task(username, post_id):
    post = db.session.query(Post).filter((Post.id == post_id)).first()
    data = [
        ["id", "title", "caption", "username", "image_url", "timestamp"],
        [post.id, post.title, post.caption, post.username, post.image_url, post.timestamp],
    ]
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    user_email = db.session.query(User).filter(User.username == username).first().email
    message = Mail(
        from_email = 'theraidercomes1@gmail.com',
        to_emails = user_email,
        subject = 'Export done alert',
        html_content = f"You Blog with ID {post_id} has been exported",
    )
    try:
        sg = SendGridAPIClient(api_key="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")
        sg.send(message)
    except Exception as e:
        print(e.message)
    return output.getvalue()

@app.route("/api/get/blog/<username>")
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def export_blog_csv(username):
    post_id = request.args.get('post_id')
    task = export_blog_to_csv_task.delay(username, post_id)
    output = task.get()
    response = make_response(output)
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.mimetype = 'text/csv'
    return response
    
    
    
    
    
    
