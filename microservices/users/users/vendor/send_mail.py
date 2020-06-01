"""
This file contains business logic to send the mail using SMTP server
Author: Akshaya Revaskar
Date: 28/04/2020
"""

# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from ...users_env import Configuration
configuration = Configuration()


class SendMail:

    def __init__(self):
        pass

    def send_mail(self, to_mail, username, host, port, short, html_file_name):
        try:

            report_file = open(html_file_name)
            html = report_file.read().format(username=username,
                                             host=host,
                                             port=port,
                                             short=short)

            # create message object instance
            msg = MIMEMultipart('alternative')

            # setup the parameters of the message
            password = configuration.MICRO_EMAIL_PASSWORD
            msg['From'] = configuration.MICRO_EMAIL_FROM
            msg['To'] = to_mail
            msg['Subject'] = "Link"

            message = "Hello"

            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(message, 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            # Send the message via local SMTP server.
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(msg['From'], password)

            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()

            print("successfully sent email to %s:" % (msg['To']))

        except Exception as e:
            print(e)



