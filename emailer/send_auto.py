# 自动发送邮件
# 目前只是适配了QQ邮箱，其他邮箱需要自己修改

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime

# 读取报告内容
def read_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 发送邮件
def send_email(subject, body, to_email):
    from_email = "bx33661@qq.com"
    password = "nrjtzhecxgypcbae"  # 替换为你的QQ邮箱授权码

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
        print(f"[{current_time}]邮件发送失败: {e}")

# 定期任务
def send_weekly_report():
    report_content = read_report("report.txt")
    subject = "项目进度报告"
    to_email = "bx33661@gmail.com"
    send_email(subject, report_content, to_email)

# 每30秒发送一次报告
schedule.every(30).seconds.do(send_weekly_report)

# 运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)  # 每秒检查一次