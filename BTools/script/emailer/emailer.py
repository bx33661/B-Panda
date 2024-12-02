# 自动发送邮件和自动回复邮件
# 目前只是适配了QQ邮箱，其他邮箱需要自己修改

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import imaplib
import email
import argparse
import sys

# 读取报告内容
def read_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 发送邮件
def send_email(subject, body, to_email, from_email, password):
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))
    
    # 连接到SMTP服务器并发送邮件
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
        print(f"[{current_time}]邮件发送失败: {e}")

# 定期任务
def send_weekly_report(from_email, password):
    report_content = read_report("report.txt")
    subject = "项目进度报告"
    to_email = "bx33661@gmail.com"
    send_email(subject, report_content, to_email, from_email, password)

# 连接到IMAP服务器
def connect_to_imap(from_email, password):
    mail = imaplib.IMAP4_SSL("imap.qq.com", 993)
    mail.login(from_email, password)
    mail.select("inbox")
    return mail

# 连接到SMTP服务器
def connect_to_smtp(from_email, password):
    server = smtplib.SMTP("smtp.qq.com", 587)
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
def send_reply(server, to_email, subject, body, from_email):
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
def auto_reply(from_email, password, reply_body, keywords):
    keywords = list(keywords.split(","))
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
                
                # 检查关键词
                for keyword in keywords:
                    if keyword in email_body:
                        reply_subject = f"Re: {email_subject}"
                    send_reply(server, email_from, reply_subject, reply_body, from_email)
    
    mail.logout()
    server.quit()

# 主函数
def main():
    print("""
 ________                       __ __                   
/        |                     /  /  |                  
$$$$$$$$/ _____  ____   ______ $$/$$ | ______   ______  
$$ |__   /     \/    \ /      \/  $$ |/      \ /      \ 
$$    |  $$$$$$ $$$$  |$$$$$$  $$ $$ /$$$$$$  /$$$$$$  |
$$$$$/   $$ | $$ | $$ |/    $$ $$ $$ $$    $$ $$ |  $$/ 
$$ |_____$$ | $$ | $$ /$$$$$$$ $$ $$ $$$$$$$$/$$ |      
$$       $$ | $$ | $$ $$    $$ $$ $$ $$       $$ |      
$$$$$$$$/$$/  $$/  $$/ $$$$$$$/$$/$$/ $$$$$$$/$$/       
Usage:(目前只支持QQ邮箱，其他邮箱需要自己修改，qq邮箱需要开启SMTP服务)
    -s 定时发送报告任务
    -r 自动回复邮件任务
项目具体使用方法见：https://www.bx33661.com
                  """)
    parser = argparse.ArgumentParser(description="邮件自动化工具")
    parser.add_argument('-s', '--send', action='store_true', help='定时发送报告任务')
    parser.add_argument('-r', '--reply', action='store_true', help='自动回复邮件任务')
    args = parser.parse_args()

    #from_email = input("请输入发送邮箱: ")
    #password = input("请输入邮箱密码: ")
    model = sys.argv[1]
    if len(sys.argv) < 2:
        print("请输入正确的参数,使用-h查看帮助")
        sys.exit(1)

    if model == "-h":
        print("Usage:(目前只支持QQ邮箱，其他邮箱需要自己修改，qq邮箱需要开启SMTP服务)")
        print("    -s 定时发送报告任务")
        print("    -r 自动回复邮件任务")
        sys.exit(1)

    
    if model == "-s":
        from_email = input("请输入发送邮箱: ")
        password = input("请输入邮箱密码: ")
        send_email_time = input("请输入发送时间间隔(分钟): ")
        if args.send:
            schedule.every(send_email_time).minutes.do(send_weekly_report, from_email, password)
        print("定时发送报告任务已启动")

    if model == "-r":
        from_email = input("请输入发送邮箱: ")
        password = input("请输入邮箱密码: ")
        keywords = input("请输入关键词(多个关键词用逗号隔开): ")
        reply_body = input("请输入回复内容: ")
        schedule.every(30).seconds.do(auto_reply, from_email, password, reply_body, keywords)
        print("自动回复邮件任务已启动")

    # 运行调度器
    while True:
        schedule.run_pending()
        time.sleep(1)  # 每秒检查一次

if __name__ == '__main__':
    main()