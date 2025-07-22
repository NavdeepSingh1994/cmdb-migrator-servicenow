from fpdf import FPDF
from pathlib import Path

def create_pdf_report(df, filename="cmdb_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="CMDB Import Report", ln=True, align="C")
    pdf.ln(10)

    for i, row in df.iterrows():
        line = f"{row['Name']} -> {row['target_table']} ({row['Environment']})"
        pdf.cell(200, 10, txt=line, ln=True)

    output_path = Path("output")
    output_path.mkdir(exist_ok=True)
    path = output_path / filename
    pdf.output(str(path))
    return path
