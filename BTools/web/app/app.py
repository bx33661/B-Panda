from flask import Flask, request, render_template, redirect, url_for, flash
from routes import pdf_routes, email_routes, find_routes, bs_routes,system_monitor_routes,network_routes
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

app = Flask(__name__)

# 从环境变量获取密钥，如果没有则使用默认值
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'bx33661')

# 配置日志
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/btools.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('BTools startup')

# 注册路由
app.register_blueprint(pdf_routes.bp)
app.register_blueprint(email_routes.bp)
app.register_blueprint(find_routes.bp)
app.register_blueprint(bs_routes.bp)
app.register_blueprint(system_monitor_routes.bp)
app.register_blueprint(network_routes.bp)

# 全局错误处理
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Internal server error'), 500

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)