import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from portfolios.forms.forms import MailForm
import os


def send_email(form: MailForm):

    message = MIMEMultipart()
    message['From'] = form.email.data
    message['To'] = os.getenv('MAIL_USERNAME')
    message['Subject'] = f'New contact message from {form.name.data}'
    mail_content = form.message.data
    message.attach(MIMEText(mail_content, 'plain'))

    with smtplib.SMTP(host=os.getenv('MAIL_SERVER'), port=587) as conn:
        conn.starttls()
        conn.login(user=os.getenv('MAIL_USERNAME'),
                   password=os.getenv('MAIL_PASSWORD'))
        conn.sendmail(from_addr=os.getenv('MAIL_USERNAME'),
                      to_addrs=form.email.data, msg=message.as_string())
