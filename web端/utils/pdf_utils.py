import os
from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_pdfs(input_folder, output_file):
    pdf_writer = PdfWriter()
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def add_watermark(input_file, output_file, watermark_text):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]
    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def create_watermark(text):
    c = canvas.Canvas("watermark.pdf", pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 50)
    c.setFillColorRGB(0.5, 0.5, 0.5, 0.5)
    c.rotate(45)
    c.drawString(100, height - 100, text)
    c.save()
    return PdfReader("watermark.pdf")

def extract_text(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(text)

def split_pdf(input_file, output_folder):
    pdf_reader = PdfReader(input_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)

def encrypt_pdf(input_file, output_file, password):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    pdf_writer.encrypt(password)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def rotate_pdf(input_file, output_file, degrees):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        page.rotate(degrees)
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def crop_pdf(input_file, output_file, box):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        page.cropbox.lower_left = (box[0], box[1])
        page.cropbox.upper_right = (box[2], box[3])
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def compress_pdf(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    pdf_writer.compress_content_streams()
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def extract_pages(input_file, output_file, page_range):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    if '-' in page_range:
        start, end = map(int, page_range.split('-'))
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    else:
        page_num = int(page_range) - 1
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)