from flask import request
from flask import make_response
from flask_cors import cross_origin
from app import celery
from app import app, token_required
from io import StringIO
import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from celery.schedules import crontab
from models.models import User, db, Post, Followers
from sendgrid.helpers.mail import Mail
import datetime
from flask import render_template

# SCHEDULING TASK FOR DAILY ALERT
@celery.on_after_finalize.connect
def setup_periodic_email_task(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='0', hour='17'),
        send_email_to_user.s(),
        name="At every 10"
    )

# SCHEDULING TASK FOR MONTHLY REPORT
@celery.on_after_finalize.connect
def setup_periodic_email_task(sender, **kwargs):
    sender.add_periodic_task(
        crontab(day_of_month='1', hour='0', minute='0'),
        send_month_report_to_users.s(),
        name='monthly_report'
    )

####################################
# DAILY ALERT TASK                 #
####################################

def get_user_emails_posted_not_today():
    dt = datetime.datetime.now().strftime('%d/%m/%Y') + "%"
    today_posts = db.session.query(Post).filter(Post.timestamp.like(dt)).all()
    today_posts_users = set([post.username for post in today_posts])
    all_users = db.session.query(User).all()
    all_users_name_email = [(user.username, user.email) for user in all_users]
    users_not_posted_today = []
    for user, email in all_users_name_email:
        if user not in today_posts_users:
            users_not_posted_today.append((user, email))
    return users_not_posted_today

@celery.task()
def send_email_to_user():
    print("SENDING DAILY EMAILS TASK IS BEING EXECUTED")
    emails_to_send = get_user_emails_posted_not_today()
    # print("--------------------------------------------------------------")
    sg_api_key = "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"
    from_email = 'theraidercomes1@gmail.com'
    to_email = [x[1] for x in emails_to_send]
    subject = 'BlogLite remembers you'
    html_content = '<p>We see you have not posted anything today, hop onto bloglite to express yourselves</p>'

    # Create the email message
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content)
    # Initialize the SendGrid client
    sg = SendGridAPIClient(api_key=sg_api_key)
    # Send the email message
    sg.send(message)

####################################
# MONTHLY REPORT GENERATION TASK   #
####################################

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



################################
# EXPORT ASYNC JOB             #
################################
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
    
    
    
    
    
    
