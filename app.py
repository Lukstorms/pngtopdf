import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_png_to_pdf(png_path, pdf_path):
    image = Image.open(png_path)
    c = canvas.Canvas(pdf_path, pagesize=image.size)
    c.drawImage(png_path, 0, 0, width=image.width, height=image.height)
    c.save()


def main():
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")

    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".PNG"):
            png_path = os.path.join(input_folder, filename)
            pdf_path = os.path.join(output_folder, filename.replace(".PNG", ".PDF"))
            convert_png_to_pdf(png_path, pdf_path)
            print("Converted {} to {}".format(filename, pdf_path))


if __name__ == "__main__":
    main()
    input("Conversion completed. Press Enter to exit.")
