from flask import Blueprint, render_template, request, jsonify
import socket
import subprocess
import platform

bp = Blueprint('network_routes', __name__)

@bp.route('/network/index')
def network_index():
    return render_template('network.html')

@bp.route('/network/ping', methods=['POST'])
def ping_test():
    host = request.form.get('host')
    try:
        # 根据操作系统选择ping命令参数
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '4', host]
        
        # 执行ping命令
        result = subprocess.run(command, 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        
        return jsonify({
            'success': True,
            'result': result.stdout
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@bp.route('/network/port', methods=['POST'])
def port_scan():
    host = request.form.get('host')
    port = int(request.form.get('port'))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        
        status = '开放' if result == 0 else '关闭'
        return jsonify({
            'success': True,
            'result': f'端口 {port} 状态: {status}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@bp.route('/network/dns', methods=['POST'])
def dns_lookup():
    host = request.form.get('host')
    try:
        ip = socket.gethostbyname(host)
        return jsonify({
            'success': True,
            'result': f'域名 {host} 解析到 IP: {ip}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }) 