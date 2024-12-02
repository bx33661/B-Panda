from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.pdf_utils import merge_pdfs, add_watermark, extract_text, split_pdf, encrypt_pdf, rotate_pdf, crop_pdf, compress_pdf, extract_pages

bp = Blueprint('pdf_routes', __name__, url_prefix='/pdf')

@bp.route('/', methods=['GET'])
def pdf_index():
    return render_template('pdf.html')

@bp.route('/', methods=['POST'])
def pdf_operations():
    action = request.form['action']
    input_file = request.files['input_file']
    output_file = request.form['output_file']
    watermark_text = request.form.get('watermark_text')
    password = request.form.get('password')
    degrees = request.form.get('degrees')
    box = request.form.get('box')
    page_range = request.form.get('page_range')
    input_folder = request.form.get('input_folder')
    output_folder = request.form.get('output_folder')

    if action == 'merge':
        if not input_folder:
            flash('合并PDF时必须提供输入文件夹')
        else:
            merge_pdfs(input_folder, output_file)
            flash('PDF文件已合并')
    elif action == 'add_watermark':
        if not watermark_text:
            flash('添加水印时必须提供水印文本')
        else:
            add_watermark(input_file.filename, output_file, watermark_text)
            flash('水印已添加')
    elif action == 'extract_text':
        extract_text(input_file.filename, output_file)
        flash('文本已提取')
    elif action == 'split':
        if not output_folder:
            flash('拆分PDF时必须提供输出文件夹')
        else:
            split_pdf(input_file.filename, output_folder)
            flash('PDF文件已拆分')
    elif action == 'encrypt':
        if not password:
            flash('加密时必须提供密码')
        else:
            encrypt_pdf(input_file.filename, output_file, password)
            flash('PDF文件已加密')
    elif action == 'rotate':
        if not degrees:
            flash('旋转时必须提供旋转角度')
        else:
            rotate_pdf(input_file.filename, output_file, int(degrees))
            flash('PDF文件已旋转')
    elif action == 'crop':
        if not box:
            flash('裁剪时必须提供边界')
        else:
            box = [float(x) for x in box.split(',')]
            crop_pdf(input_file.filename, output_file, box)
            flash('PDF文件已裁剪')
    elif action == 'compress':
        compress_pdf(input_file.filename, output_file)
        flash('PDF文件已压缩')
    elif action == 'extract_pages':
        if not page_range:
            flash('提取页面时必须提供页面范围')
        else:
            extract_pages(input_file.filename, output_file, page_range)
            flash('PDF文件的特定页面已提取')

    return redirect(url_for('pdf_routes.pdf_index'))