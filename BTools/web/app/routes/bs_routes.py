from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template
from utils.bs_utils import encode_base64, decode_base64

bp = Blueprint('bs_routes', __name__, url_prefix='/base')

@bp.route('/', methods=['GET'])
def bs_index():
    return render_template('bs.html')

@bp.route('/encode', methods=['POST'])
def encode():
    data = request.json
    input_string = data.get('input_string', '')
    if not input_string:
        flash('请输入有效的字符串进行编码')
        return redirect(url_for('bs_routes.bs_index'))
    encoded_string = encode_base64(input_string)
    return jsonify({'encoded_string': encoded_string})

@bp.route('/decode', methods=['POST'])
def decode():
    data = request.json
    base64_string = data.get('base64_string', '')
    if not base64_string:
        flash('请输入有效的Base64字符串进行解码')
        return redirect(url_for('bs_routes.bs_index'))
    decoded_string = decode_base64(base64_string)
    return jsonify({'decoded_string': decoded_string})
