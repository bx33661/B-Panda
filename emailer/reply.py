import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import datetime

# 配置信息
from_email = "bx33661@qq.com"
password = "nrjtzhecxgypcbae"  # 替换为你的QQ邮箱授权码
smtp_server = "smtp.qq.com"
smtp_port = 587
imap_server = "imap.qq.com"
imap_port = 993

# 连接到IMAP服务器
def connect_to_imap():
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(from_email, password)
    mail.select("inbox")
    return mail

# 连接到SMTP服务器
def connect_to_smtp():
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    return server

# 读取未读邮件
def read_unread_emails(mail):
    status, messages = mail.search(None, 'UNSEEN')
    unread_msg_nums = messages[0].split()
    return unread_msg_nums

# 解析邮件内容
def parse_email(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload(decode=True).decode('utf-8')
    return ""

# 发送回复邮件
def send_reply(server, to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server.sendmail(from_email, to_email, msg.as_string())
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 自动回复邮件发送成功")
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] 自动回复邮件发送失败: {e}")

# 自动回复邮件
def auto_reply():
    mail = connect_to_imap()
    server = connect_to_smtp()
    
    unread_msg_nums = read_unread_emails(mail)
    
    for e_id in unread_msg_nums:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                email_body = parse_email(msg)
                
                # 检查关键词
                if "关键词" in email_body:
                    reply_subject = f"Re: {email_subject}"
                    reply_body = "这是自动回复的内容。"
                    send_reply(server, email_from, reply_subject, reply_body)
    
    mail.logout()
    server.quit()

# 每30秒检查一次邮件
import schedule
import time

schedule.every(30).seconds.do(auto_reply)

# 运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)  # 每秒检查一次