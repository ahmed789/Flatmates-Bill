import webbrowser
import os
from fpdf import FPDF


class PdfReport:

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pays = str(flatmate1.pays(bill=bill, flatmate=flatmate2))
        flatmate2_pays = str(flatmate2.pays(bill=bill, flatmate=flatmate1))

        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # add image
        pdf.image('files/house.png', w=40, h=40)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=1, align='C', ln=1)

        # insert period label and value
        pdf.set_font(family='Arial', size=18, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and due amount
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0)
        os.chdir("files")
        pdf.output(self.file_name)
        webbrowser.open(self.file_name)
