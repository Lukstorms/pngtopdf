import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_png_to_pdf(png_path, pdf_path):
    image = Image.open(png_path)
    c = canvas.Canvas(pdf_path, pagesize=image.size)
    c.drawImage(png_path, 0, 0, width=image.width, height=image.height)
    c.save()


def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".PNG"):
            png_path = os.path.join(input_folder, filename)
            pdf_path = os.path.join(output_folder, filename.replace(".PNG", ".PDF"))
            convert_png_to_pdf(png_path, pdf_path)
            print(f"Converted {filename} to {pdf_path}")


if __name__ == "__main__":
    input_folder = "PROTOCOLOS PETIÇÃO"  # Replace with the path to your input folder
    output_folder = "CONVERTIDOS"  # Replace with the path to your output folder
    main(input_folder, output_folder)
