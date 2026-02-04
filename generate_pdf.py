#!/usr/bin/env python3
import weasyprint
import os
from weasyprint import HTML, CSS

def generate_pdf():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'index.html')
    pdf_file = os.path.join(current_dir, 'Digivation_Company_Profile_Landscape.pdf')
    
    # CSS for landscape orientation
    landscape_css = CSS(string='''
        @page {
            size: A4 landscape;
            margin: 0.5in;
        }
    ''')
    
    # Generate PDF
    html = HTML(filename=html_file)
    html.write_pdf(pdf_file, stylesheets=[landscape_css])
    
    print(f"Landscape PDF generated: {pdf_file}")

if __name__ == "__main__":
    generate_pdf()