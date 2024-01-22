import os
import wx
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_image_to_pdf(image_path, pdf_path):
    image = Image.open(image_path)
    c = canvas.Canvas(pdf_path, pagesize=image.size)
    c.drawImage(image_path, 0, 0, width=image.width, height=image.height)
    c.save()


class PDFConverterApp(wx.App):
    def OnInit(self):
        self.frame = PDFConverterFrame(None, title="Image to PDF Converter")
        self.frame.Show()
        return True


class PDFConverterFrame(wx.Frame):
    def __init__(self, parent, title):
        super(PDFConverterFrame, self).__init__(parent, title=title, size=(400, 300))

        self.panel = wx.Panel(self)
        self.input_folder_text = wx.StaticText(self.panel, label="Selecione pasta de entrada:")
        self.input_folder_picker = wx.DirPickerCtrl(self.panel, message="Escolha pasta de entrada")
        self.output_folder_text = wx.StaticText(self.panel, label="Selecione pasta de saída:")
        self.output_folder_picker = wx.DirPickerCtrl(self.panel, message="Escolha pasta de saída")
        self.run_button = wx.Button(self.panel, label="Rodar conversão")
        self.Bind(wx.EVT_BUTTON, self.on_run, self.run_button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.input_folder_text, 0, wx.ALL, 10)
        self.sizer.Add(self.input_folder_picker, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.output_folder_text, 0, wx.ALL, 10)
        self.sizer.Add(self.output_folder_picker, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.run_button, 0, wx.ALL | wx.CENTER, 10)

        self.panel.SetSizer(self.sizer)

    def on_run(self, event):
        input_folder = self.input_folder_picker.GetPath()
        output_folder = self.output_folder_picker.GetPath()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.lower().endswith((".png", ".jpeg", ".jpg", ".PNG", ".JPEG", ".JPG")):
                image_path = os.path.join(input_folder, filename)
                pdf_filename = filename.split('.')[0] + ".pdf"
                pdf_path = os.path.join(output_folder, pdf_filename)
                convert_image_to_pdf(image_path, pdf_path)
                print(f"Converted {filename} to {pdf_filename}")
        wx.MessageBox("Conversão concluída.", "Info", wx.OK | wx.ICON_INFORMATION)
        self.Close()  # Close the application after conversion


if __name__ == "__main__":
    app = PDFConverterApp(False)
    app.MainLoop()
