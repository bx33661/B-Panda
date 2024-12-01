# routes.py

from flask import Blueprint, jsonify, request
from models import db, Website, MonitorData
from scheduler import add_job

# 创建一个 Blueprint，用来管理路由
main = Blueprint('main', __name__)

# API 路由：获取监控数据
@main.route('/api/monitor', methods=['GET'])
def get_monitor_data():
    # 查询所有监控数据
    data = MonitorData.query.order_by(MonitorData.timestamp.desc()).all()
    result = [{
        "timestamp": entry.timestamp,
        "url": entry.website.url,
        "status_code": entry.status_code,
        "response_time": entry.response_time
    } for entry in data]
    return jsonify(result)

# API 路由：添加新网站进行监控
@main.route('/api/add_website', methods=['POST'])
def add_website():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # 检查网站是否已存在
    existing_website = Website.query.filter_by(url=url).first()
    if existing_website:
        return jsonify({"message": f"Website {url} is already being monitored."}), 200

    # 将新的目标网站添加到数据库
    website = Website(url=url)
    db.session.add(website)
    db.session.commit()

    # 为新的目标网站添加一个定时监控任务
    add_job(url)
    
    return jsonify({"message": f"Website {url} added to monitoring."}), 201
