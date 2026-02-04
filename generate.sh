#!/bin/bash
echo "Generating PDF from company profile..."
source pdf_env/bin/activate
python generate_pdf.py
echo "PDF generation complete!"