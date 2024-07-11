# Flask Invoice Generator

This is a web-based invoice generator application built using Flask and ReportLab. Users can fill out a form with company and invoice details, and generate a PDF invoice.

## Features

- User-friendly web interface for entering invoice details
- Generates a PDF invoice with company logo, customer information, and order details
- Easily customizable and extendable

## Requirements

- Python 3.x
- Flask
- ReportLab

## Installation

1. **Clone the Repository**

  ```
  git clone https://github.com/your-username/InvoiceGenerator.git
  
   cd InvoiceGenerator
  ```

- Create a Virtual Environment

````
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate``


- Install Dependencies


pip install -r requirements.txt


 ## Usage

1. Run the Flask Application

    ` python app.py`

2. Access the Application

    Open your web browser and navigate to `http://localhost:5000`. You should see the invoice generator form.

3. Fill Out the Form

    Enter the necessary details, such as **company name, address, GST number, customer name, etc**.

4. Generate the Invoice

    Click the > "Generate Invoice" button to create and download the PDF invoice.


## File Structure

`InvoiceGenerator/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── logo.png (your company logo or placeholder)
├── requirements.txt
└── README.md`


## app.py

    The main Flask application file. It contains the routes and logic for generating the PDF invoice.

## templates/index.html

    The HTML template for the form where users enter invoice details.

## static/logo.png

    A placeholder for your company logo. Replace this with your actual logo if needed.

## requirements.txt

    A file listing the required Python packages.

## Customization

    * Form Fields: You can add or modify form fields in templates/index.html.

    * PDF Layout: Customize the layout and content of the generated PDF in app.py.
    
## Contributing
----
Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License
------- 
This project is licensed under the MIT License. See the LICENSE file for details.


