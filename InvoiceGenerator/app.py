from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    file_name = request.form['file_name']
    company_name = request.form['company_name']
    address = request.form['address']
    city = request.form['city']
    gst_no = request.form['gst_no']
    date = request.form['date']
    customer_name = request.form['customer_name']
    phone_no = request.form['phone_no']
    auth_sign = request.form['auth_sign']

    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=(200, 250), bottomup=0)

    pdf_canvas.line(5, 45, 195, 45)
    pdf_canvas.line(15, 120, 185, 120)
    pdf_canvas.line(35, 108, 35, 220)
    pdf_canvas.line(115, 108, 115, 220)
    pdf_canvas.line(135, 108, 135, 220)
    pdf_canvas.line(160, 108, 160, 220)
    pdf_canvas.line(15, 220, 185, 220)

    pdf_canvas.translate(10, 40)
    pdf_canvas.scale(1, -1)
    pdf_canvas.drawImage(file_name, 0, 0, width=50, height=30)
    pdf_canvas.scale(1, -1)
    pdf_canvas.translate(-10, -40)

    pdf_canvas.setFont("Times-Bold", 10)
    pdf_canvas.drawCentredString(125, 20, company_name)
    pdf_canvas.setFont("Times-Bold", 5)
    pdf_canvas.drawCentredString(125, 30, address)
    pdf_canvas.drawCentredString(125, 35, f"{city}, India")
    pdf_canvas.setFont("Times-Bold", 6)
    pdf_canvas.drawCentredString(125, 42, f"GST No: {gst_no}")

    pdf_canvas.setFont("Times-Bold", 8)
    pdf_canvas.drawCentredString(100, 55, "INVOICE")

    pdf_canvas.setFont("Times-Bold", 5)
    pdf_canvas.drawRightString(70, 70, "Invoice No.:")
    pdf_canvas.drawRightString(100, 70, "XXXXXXX")
    pdf_canvas.drawRightString(70, 80, "Customer Name:")
    pdf_canvas.drawRightString(100, 80, customer_name)
    pdf_canvas.drawRightString(70, 90, "Date:")
    pdf_canvas.drawRightString(100, 90, date)
    pdf_canvas.drawRightString(70, 100, "Phone No.:")
    pdf_canvas.drawRightString(100, 100, phone_no)

    pdf_canvas.roundRect(15, 108, 170, 130, 10, fill=0)
    pdf_canvas.drawCentredString(25, 118, "S.No.")
    pdf_canvas.drawCentredString(75, 118, "Orders")
    pdf_canvas.drawCentredString(125, 118, "Price")
    pdf_canvas.drawCentredString(148, 118, "Qty.")
    pdf_canvas.drawCentredString(173, 118, "Total")

    pdf_canvas.drawRightString(180, 228, auth_sign)
    pdf_canvas.drawRightString(180, 235, "Signature")

    pdf_canvas.showPage()
    pdf_canvas.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='Invoice.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
