from flask import Flask, jsonify, request, render_template
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from apscheduler.triggers.interval import IntervalTrigger
from models import db, Website, MonitorData
from config import Config  # 导入配置类

app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 用于存储监控数据和目标网站
monitor_data = []
target_websites = []

# 创建后台任务调度器
scheduler = BackgroundScheduler()

def check_website(url):
    with app.app_context():  # 设置应用上下文
        try:
            response = requests.get(url)
            response_time = response.elapsed.total_seconds()
            status_code = response.status_code
        except requests.RequestException as e:
            response_time = None
            status_code = 'Error'
            print(f"Error checking {url}: {e}")

        # 获取或创建网站记录
        website = Website.query.filter_by(url=url).first()
        if not website:
            website = Website(url=url)
            db.session.add(website)
            db.session.commit()

        # 创建监控数据记录
        monitor_entry = MonitorData(
            timestamp=datetime.datetime.utcnow(),
            status_code=status_code,
            response_time=response_time,
            website_id=website.id
        )
        db.session.add(monitor_entry)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add_website', methods=['POST'])
def add_website():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    if url in target_websites:
        return jsonify({"message": f"Website {url} is already being monitored."}), 200

    target_websites.append(url)
    
    # 添加定时任务
    scheduler.add_job(
        check_website, 
        IntervalTrigger(seconds=5),  # 每 5 秒检查一次
        args=[url],
        id=url  # 使用 URL 作为任务 ID，避免重复
    )
    
    return jsonify({"message": f"Website {url} added to monitoring."}), 201

@app.route('/api/monitor', methods=['GET'])
def get_monitor_data():
    with app.app_context():  # 设置应用上下文
        data = MonitorData.query.all()
        monitor_data_list = [
            {
                "id": entry.id,
                "timestamp": entry.timestamp.isoformat(),
                "status_code": entry.status_code,
                "response_time": entry.response_time,
                "website_id": entry.website_id,
                "url": entry.website.url  # 通过 relationship 获取 url
            }
            for entry in data
        ]
        return jsonify(monitor_data_list), 200

@app.route('/api/debug', methods=['GET'])
def debug_monitor_data():
    with app.app_context():  # 设置应用上下文
        data = MonitorData.query.all()
        debug_data_list = [
            {
                "id": entry.id,
                "timestamp": entry.timestamp.isoformat(),
                "status_code": entry.status_code,
                "response_time": entry.response_time,
                "website_id": entry.website_id,
                "url": entry.website.url if entry.website else "No website found"
            }
            for entry in data
        ]
        return jsonify(debug_data_list), 200

if __name__ == '__main__':
    # 创建数据库表
    with app.app_context():
        db.create_all()
        print("Database tables created.")
    
    # 启动定时任务调度器
    scheduler.start()
    app.run(debug=True)