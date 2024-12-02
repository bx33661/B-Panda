import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import imaplib
import email


def read_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def send_email(subject, body, to_email, from_email, password):
    smtp_server = "smtp.qq.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 邮件发送成功")
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 邮件发送失败: {e}")


def send_weekly_report(from_email, password):
    report_content = read_report("report.txt")
    subject = "项目进度报告"
    to_email = "bx33661@gmail.com"
    send_email(subject, report_content, to_email, from_email, password)


def connect_to_imap(from_email, password):
    mail = imaplib.IMAP4_SSL("imap.qq.com", 993)
    mail.login(from_email, password)
    mail.select("inbox")
    return mail


def connect_to_smtp(from_email, password):
    server = smtplib.SMTP("smtp.qq.com", 587)
    server.starttls()
    server.login(from_email, password)
    return server


def read_unread_emails(mail):
    status, messages = mail.search(None, 'UNSEEN')
    unread_msg_nums = messages[0].split()
    return unread_msg_nums


def parse_email(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload(decode=True).decode('utf-8')
    return ""


def auto_reply(from_email, password, reply_body, keywords):
    mail = connect_to_imap(from_email, password)
    server = connect_to_smtp(from_email, password)

    unread_msg_nums = read_unread_emails(mail)

    for e_id in unread_msg_nums:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                email_body = parse_email(msg)

                for keyword in keywords.split(','):
                    if keyword.strip() in email_body:
                        reply_subject = f"Re: {email_subject}"
                        send_email(reply_subject, reply_body, email_from, from_email, password)

    mail.logout()
    server.quit()