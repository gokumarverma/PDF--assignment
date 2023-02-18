from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob(f'Text Files\*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for path in filepaths:
    filename = Path(path).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=12, txt=filename , border=0, ln=1,align='L')
    with open(path,'r') as file:
        data = file.readline()
        pdf.set_font(family='Times', style='', size=12)
        pdf.multi_cell(w=0, h=8, txt=data, border=0, align='L')

pdf.output('Assignment_completed.pdf')





