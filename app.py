
from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genera_pdf', methods=['POST'])
def genera_pdf():
    cliente = request.form['cliente']
    materiale = request.form['materiale']

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cryotech Bolla di Lavoro", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Materiale: {materiale}", ln=True)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, as_attachment=True, download_name="bolla_di_lavoro.pdf")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
