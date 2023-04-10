# Importing necessary libraries
import os
from pdf2image import convert_from_path

# Setting up the paths
input_directory = "OutputSplitPDF"
output_directory = "OutputPDFJPG"

# Create Output Directory, if it doesn't exist
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# Iterate through all PDFs in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.pdf'):
        # Convert PDF to images
        # Please install poppler and place it at "poppler_path" link --> https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image
        images = convert_from_path(input_directory + '/' + filename, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

        # Save each image in the output directory
        for i, image in enumerate(images):
            image.save(output_directory + '/' + filename + '.jpg', 'JPEG')