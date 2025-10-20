import os
import subprocess
from pathlib import Path

# Input and output folders
input_folder = './'
output_folder = './reduced'
output_folder_png = './reduced_png'

# Create output folders if they don't exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_folder_png, exist_ok=True)

# Get all PDF files
pdf_files = list(Path(input_folder).glob('*.pdf'))

print(f"Found {len(pdf_files)} PDF files")

for pdf_file in pdf_files:
    input_path = str(pdf_file)
    output_pdf_path = os.path.join(output_folder, pdf_file.name)
    output_png_path = os.path.join(output_folder_png, pdf_file.stem + '.png')
    
    # 1. Compress PDF
    gs_pdf_command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/ebook',        # '-dPDFSETTINGS=/screen',  # Use /ebook for good quality, /printer for higher or /screen

        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_pdf_path}',
        input_path
    ]
    
    # 2. Convert to PNG
    gs_png_command = [
        'gs',
        '-sDEVICE=png16m',
        '-dTextAlphaBits=4',
        '-dGraphicsAlphaBits=4',
        '-r300',  # 300 DPI resolution
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_png_path}',
        input_path
    ]
    
    try:
        # Compress PDF
        subprocess.run(gs_pdf_command, check=True)
        
        # Convert to PNG
        //subprocess.run(gs_png_command, check=True)
        
        # Check file sizes
        original_size = os.path.getsize(input_path) / 1024
        compressed_size = os.path.getsize(output_pdf_path) / 1024
        png_size = os.path.getsize(output_png_path) / 1024
        reduction = (1 - compressed_size/original_size) * 100
        
        print(f"{pdf_file.name}:")
        print(f"  PDF: {original_size:.1f} KB -> {compressed_size:.1f} KB ({reduction:.1f}% reduction)")
        print(f"  PNG: {png_size:.1f} KB")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {pdf_file.name}: {e}")

print("Done!")