from flask import Blueprint, request, jsonify, render_template
import psutil
import time
from datetime import datetime
import threading
import queue

bp = Blueprint('system_monitor', __name__, url_prefix='/sysmon')

# 存储监控数据
monitoring_data = queue.Queue(maxsize=100)
alert_thresholds = {
    'cpu': 80,  # CPU使用率阈值
    'memory': 80,  # 内存使用率阈值
    'disk': 90,  # 磁盘使用率阈值
}

def collect_system_metrics():
    """收集系统指标"""
    while True:
        try:
            # CPU信息
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_freq = psutil.cpu_freq()
            
            # 内存信息
            memory = psutil.virtual_memory()
            
            # 磁盘信息
            disk = psutil.disk_usage('/')
            
            # 网络信息
            network = psutil.net_io_counters()
            
            # 进程信息
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    pinfo = proc.info
                    if pinfo['cpu_percent'] > 0:
                        processes.append(pinfo)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'cpu': {
                    'percent': cpu_percent,
                    'freq': cpu_freq.current if cpu_freq else 0
                },
                'memory': {
                    'total': memory.total,
                    'available': memory.available,
                    'percent': memory.percent
                },
                'disk': {
                    'total': disk.total,
                    'used': disk.used,
                    'free': disk.free,
                    'percent': disk.percent
                },
                'network': {
                    'bytes_sent': network.bytes_sent,
                    'bytes_recv': network.bytes_recv
                },
                'processes': sorted(processes, 
                                 key=lambda x: x['cpu_percent'], 
                                 reverse=True)[:10]  # Top 10 processes
            }
            
            # 检查告警
            alerts = []
            if data['cpu']['percent'] > alert_thresholds['cpu']:
                alerts.append(f"CPU usage is high: {data['cpu']['percent']}%")
            if data['memory']['percent'] > alert_thresholds['memory']:
                alerts.append(f"Memory usage is high: {data['memory']['percent']}%")
            if data['disk']['percent'] > alert_thresholds['disk']:
                alerts.append(f"Disk usage is high: {data['disk']['percent']}%")
            
            data['alerts'] = alerts
            
            # 如果队列满了，移除最旧的数据
            if monitoring_data.full():
                monitoring_data.get()
            monitoring_data.put(data)
            
            time.sleep(2)  # 每2秒收集一次数据
            
        except Exception as e:
            print(f"Error collecting metrics: {str(e)}")

# 启动监控线程
monitor_thread = threading.Thread(target=collect_system_metrics)
monitor_thread.daemon = True
monitor_thread.start()

@bp.route('/')
def index():
    return render_template('sysmon.html')

@bp.route('/metrics')
def get_metrics():
    # 获取最新的监控数据
    data = []
    while not monitoring_data.empty():
        data.append(monitoring_data.get())
    return jsonify(data)

@bp.route('/thresholds', methods=['GET', 'POST'])
def manage_thresholds():
    if request.method == 'POST':
        new_thresholds = request.get_json()
        for key, value in new_thresholds.items():
            if key in alert_thresholds and isinstance(value, (int, float)):
                alert_thresholds[key] = value
        return jsonify(alert_thresholds)
    return jsonify(alert_thresholds)
