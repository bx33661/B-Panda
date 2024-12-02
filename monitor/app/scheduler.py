# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
from models import db, Website, MonitorData

# 创建调度器实例
scheduler = BackgroundScheduler()

# 定时任务：检查网站状态
def check_website(url):
    try:
        response = requests.get(url, timeout=5)  # 设置请求超时为 5 秒
        status_code = response.status_code
        response_time = response.elapsed.total_seconds()
    except requests.exceptions.RequestException as e:
        status_code = "Error"
        response_time = None

    # 查找网站并保存监控数据
    website = Website.query.filter_by(url=url).first()
    if website:
        monitor_entry = MonitorData(
            status_code=status_code,
            response_time=response_time,
            website=website
        )
        db.session.add(monitor_entry)
        db.session.commit()

# 启动调度器，间隔 10 秒检查每个网站的状态
def start_scheduler():
    scheduler.start()

def add_job(url):
    scheduler.add_job(
        check_website,
        IntervalTrigger(seconds=10),  # 每 10 秒检查一次
        args=[url],
        id=url  # 使用 URL 作为任务 ID，避免重复
    )
