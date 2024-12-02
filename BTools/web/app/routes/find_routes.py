from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.find_utils import search_files_by_name, search_files_by_content

bp = Blueprint('find_routes', __name__, url_prefix='/find')

@bp.route('/', methods=['GET'])
def find_index():
    return render_template('find.html')

@bp.route('/', methods=['POST'])
def find_files():
    directory = request.form['directory']
    keyword = request.form['keyword']
    mode = request.form.get('mode', 'name')
    output_file = request.form.get('output_file')

    if mode == 'name':
        results = search_files_by_name(directory, keyword)
    elif mode == 'content':
        results = search_files_by_content(directory, keyword)

    if results:
        flash('找到以下文件包含关键词:')
        for result in results:
            flash(result)
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for result in results:
                    f.write(result + '\n')
            flash(f"结果已保存到: {output_file}")
    else:
        flash('没有找到包含关键词的文件。')

    return redirect(url_for('find_routes.find_index'))