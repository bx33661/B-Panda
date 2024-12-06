import os
import argparse
from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_pdfs(input_folder, output_file):
    pdf_writer = PdfWriter()

    # 遍历文件夹中的所有PDF文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            pdf_reader = PdfReader(pdf_path)
            # 将每个PDF文件的每一页添加到输出文件中
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    # 写入合并后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def add_watermark(input_file, output_file, watermark_text):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 创建水印PDF
    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]

    # 将水印添加到每一页
    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    # 写入添加水印后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def create_watermark(text):
    c = canvas.Canvas("watermark.pdf", pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 50)
    c.setFillColorRGB(0.5, 0.5, 0.5, 0.5)  # 半透明的灰色
    c.rotate(45)  # 旋转45度
    c.drawString(100, height - 100, text)
    c.save()
    return PdfReader("watermark.pdf")

def extract_text(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    text = ""

    # 提取每一页的文本
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

    # 写入提取的文本到文件
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(text)

def split_pdf(input_file, output_folder):
    pdf_reader = PdfReader(input_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 拆分每一页并保存为单独的PDF文件
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)

def encrypt_pdf(input_file, output_file, password):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 将每一页添加到输出文件中
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # 加密PDF文件
    pdf_writer.encrypt(password)

    # 写入加密后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def rotate_pdf(input_file, output_file, degrees):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 旋转每一页
    for page in pdf_reader.pages:
        page.rotate(degrees)
        pdf_writer.add_page(page)

    # 写入旋转后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def crop_pdf(input_file, output_file, box):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 裁剪每一页
    for page in pdf_reader.pages:
        page.cropbox = box
        pdf_writer.add_page(page)

    # 写入裁剪后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def compress_pdf(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 压缩每一页
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # 写入压缩后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def extract_pages(input_file, output_file, page_range):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    # 提取特定页面
    if '-' in page_range:
        start, end = map(int, page_range.split('-'))
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    else:
        page_num = int(page_range) - 1
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # 写入提取页面后的PDF文件
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def main():
    print("""
 _______       __  ______                  
/       \     /  |/      \                 
$$$$$$$  |____$$ /$$$$$$  ______   ______  
$$ |__$$ /    $$ $$ |_ $$/      \ /      \ 
$$    $$/$$$$$$$ $$   | /$$$$$$  /$$$$$$  |
$$$$$$$/$$ |  $$ $$$$/  $$    $$ $$ |  $$/ 
$$ |    $$ \__$$ $$ |   $$$$$$$$/$$ |      
$$ |    $$    $$ $$ |   $$       $$ |      
$$/      $$$$$$$/$$/     $$$$$$$/$$/                                           

Usage:

    -a 操作类型: merge, add_watermark, extract_text, split, encrypt, rotate, crop, compress, extract_pages
    -i 输入文件或文件夹路径
    -o 输出文件路径
    -w 水印文本（仅在添加水印时使用）
    -p 密码（仅在加密时使用）
    -d 旋转角度（仅在旋转时使用）
    -b 裁剪边界（仅在裁剪时使用）
    -r 页面范围（仅在提取页面时使用）
具体使用方法见：https://www.bx33661.com/

    """)
    parser = argparse.ArgumentParser(description='PDF自动化工具')
    parser.add_argument('-a', '--action', choices=['merge', 'add_watermark', 'extract_text', 'split', 'encrypt', 'rotate', 'crop', 'compress', 'extract_pages'], required=True, help='操作类型: merge, add_watermark, extract_text, split, encrypt, rotate, crop, compress, extract_pages')
    parser.add_argument('-i', '--input', required=True, help='输入文件或文件夹路径')
    parser.add_argument('-o', '--output', required=True, help='输出文件路径')
    parser.add_argument('-w', '--watermark', help='水印文本（仅在添加水印时使用）')
    parser.add_argument('-p', '--password', help='密码（仅在加密时使用）')
    parser.add_argument('-d', '--degrees', type=int, choices=[90, 180, 270], help='旋转角度（90, 180, 270）')
    parser.add_argument('-b', '--box', help='裁剪边界（格式：left,top,right,bottom）')
    parser.add_argument('-r', '--page_range', help='页面范围（格式：start-end 或 page_number）')

    args = parser.parse_args()

    if args.action == 'merge':
        merge_pdfs(args.input, args.output)
        print(f"PDF文件已合并到 {args.output}")
    elif args.action == 'add_watermark':
        if not args.watermark:
            parser.error("添加水印时必须提供水印文本 (-w)")
        add_watermark(args.input, args.output, args.watermark)
        print(f"水印已添加到 {args.output}")
    elif args.action == 'extract_text':
        extract_text(args.input, args.output)
        print(f"文本已提取到 {args.output}")
    elif args.action == 'split':
        split_pdf(args.input, args.output)
        print(f"PDF文件已拆分到 {args.output} 文件夹中")
    elif args.action == 'encrypt':
        if not args.password:
            parser.error("加密时必须提供密码 (-p)")
        encrypt_pdf(args.input, args.output, args.password)
        print(f"PDF文件已加密到 {args.output}")
    elif args.action == 'rotate':
        if not args.degrees:
            parser.error("旋转时必须提供旋转角度 (-d)")
        rotate_pdf(args.input, args.output, args.degrees)
        print(f"PDF文件已旋转到 {args.output}")
    elif args.action == 'crop':
        if not args.box:
            parser.error("裁剪时必须提供边界 (-b)")
        box = [float(x) for x in args.box.split(',')]
        crop_pdf(args.input, args.output, box)
        print(f"PDF文件已裁剪到 {args.output}")
    elif args.action == 'compress':
        compress_pdf(args.input, args.output)
        print(f"PDF文件已压缩到 {args.output}")
    elif args.action == 'extract_pages':
        if not args.page_range:
            parser.error("提取页面时必须提供页面范围 (-r)")
        extract_pages(args.input, args.output, args.page_range)
        print(f"PDF文件的特定页面已提取到 {args.output}")

if __name__ == '__main__':
    main()