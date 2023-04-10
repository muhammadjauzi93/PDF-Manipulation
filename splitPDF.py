"""
1. Open directory
2. Split PDF pages in directory
3. Save output in another directory
"""

# Importing necessary libraries
import os
from PyPDF2 import PdfWriter, PdfReader

# Setting up the paths
input_directory = "InputPDF"
output_directory = "OutputSplitPDF"

# Create Output Directory, if it doesn't exist
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# Iterate through all PDFs in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.pdf'):
        # Create input and output PDF objects
        input_pdf = PdfReader(open(input_directory + '/' + filename, 'rb'))
        output_pdf = PdfWriter()

        # Split PDF by pages
        for page_num in range(len(input_pdf.pages)):
            output_pdf.add_page(input_pdf.pages[page_num])

            # Save each page in the output directory
            with open(output_directory + '/' + filename + '_page_' + str(page_num) + '.pdf', 'wb') as f:
                output_pdf.write(f)