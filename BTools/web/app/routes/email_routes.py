from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.email_utils import send_weekly_report, auto_reply

bp = Blueprint('email_routes', __name__, url_prefix='/email')

@bp.route('/', methods=['GET'])
def email_index():
    return render_template('email.html')

@bp.route('/', methods=['POST'])
def email_operations():
    action = request.form['action']
    from_email = request.form['from_email']
    password = request.form['password']
    if action == 'send':
        send_email_time = request.form['send_email_time']
        # schedule.every(int(send_email_time)).minutes.do(send_weekly_report, from_email, password)
        flash('定时发送报告任务已启动')
    elif action == 'reply':
        keywords = request.form['keywords']
        reply_body = request.form['reply_body']
        # schedule.every(30).seconds.do(auto_reply, from_email, password, reply_body, keywords)
        flash('自动回复邮件任务已启动')
    return redirect(url_for('email_routes.email_index'))