from fpdf import FPDF
import pandas as pd

# Create an instance from a fpdf class
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for item in range(row["Pages"]):
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=15)
        # Set a color to a text (In parameters, should put a RGB values)
        pdf.set_text_color(254, 100, 100)
        # Set a cell
        pdf.cell(w=0, h=15, txt=row["Topic"], align="L", ln=1)
        # Set a line
        # x1: coordinates a distance from beginning of line (left to right)
        # x2: coordinates from end point of line on the left (from top to line)
        # x3: lenght of the lin
        # x4: coordinates from end point of line on the right (from top to line)
        pdf.line(10, 21, 200, 21)


pdf.output("output.pdf")
