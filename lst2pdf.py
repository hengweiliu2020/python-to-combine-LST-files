#!/usr/bin/python3

import glob
import os
from fpdf import FPDF

read_files2 = glob.glob("*.lst")
read_files2.sort()

for f in read_files2:
    lin=os.path.basename(f)
    lin2=lin.replace('lst','pdf')
    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font("Courier", size=8)
    infi = open(f, 'r')
    for x in infi:
        pdf.cell(250, 3.4, txt=x, ln=1, align='R')
    infi.close()
    pdf.output(lin2)
