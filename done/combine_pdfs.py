import os
from PyPDF2 import PdfMerger

def merge():
    # Get a list of all PDF files in the current directory
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]

    pdf_files.sort()

    # Create a PDF merger object
    pdf_merger = PdfMerger()

    # Iterate through the PDF files and merge them into one PDF
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # Output merged PDF to a new file
    output_pdf_path = 'merged.pdf'
    with open(output_pdf_path, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Merged PDF saved to {output_pdf_path}')

if __name__ == "__main__":
    merge()