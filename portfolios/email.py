import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from portfolios.forms.forms import MailForm
import os


def send_email(form: MailForm):

    message = MIMEMultipart()
    message['From'] = form.email.data
    message['To'] = os.environ.get('MAIL_USERNAME')
    message['Subject'] = f'New contact message from {form.name.data}\n Contact email:{form.email.data}'
    mail_content = form.message.data
    message.attach(MIMEText(mail_content, 'plain'))

    with smtplib.SMTP(host=os.environ.get('MAIL_SERVER'), port=os.environ.get('MAIL_PORT')) as conn:
        conn.starttls()
        conn.login(user=os.environ.get('MAIL_USERNAME'),
                   password=os.environ.get('MAIL_PASSWORD'))
        conn.sendmail(from_addr=os.environ.get('MAIL_USERNAME'),
                      to_addrs=os.environ.get('MAIL_USERNAME'), msg=message.as_string())
