from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for item in range(row["Pages"]):
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=15)
        pdf.set_text_color(254, 100, 100)
        pdf.cell(w=0, h=15, txt=row["Topic"], align="L", ln=1)

        for y in range(20, 280, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
