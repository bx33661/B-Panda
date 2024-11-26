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

    -a 操作类型: merge, add_watermark, extract_text, split
    -i 输入文件或文件夹路径

    -o 输出文件路径
    -w 水印文本（仅在添加水印时使用）
具体使用方法见：https://www.bx33661.com/

    """)
    parser = argparse.ArgumentParser(description='PDF自动化工具')
    parser.add_argument('-a', '--action', choices=['merge', 'add_watermark', 'extract_text', 'split'], required=True, help='操作类型: merge, add_watermark, extract_text, split')
    parser.add_argument('-i', '--input', required=True, help='输入文件或文件夹路径')
    parser.add_argument('-o', '--output', required=True, help='输出文件路径')
    parser.add_argument('-w', '--watermark', help='水印文本（仅在添加水印时使用）')

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

if __name__ == '__main__':
    main()