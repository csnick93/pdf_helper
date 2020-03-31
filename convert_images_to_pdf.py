import os
from PIL import Image
from pathlib import Path
from PyPDF2 import PdfFileMerger

input_path = '.'
im_files = sorted(
    [os.path.join(input_path, f) for f in os.listdir(input_path) if Path(f).suffix in ['.jpg', '.png', '.jpeg', '.pdf']])
out_file = os.path.join(input_path, 'FehlendeSteuerUnterlagen.pdf')
out_dir = os.path.dirname(out_file)

tmp_pdfs = []

rotate = False

def rotate_im(im):
    return im.rotate(90)

# convert images to pdf
for im_file in im_files:
    if Path(im_file).suffix == '.pdf':
        tmp_pdfs.append(im_file)
        continue
    im = Image.open(im_file)
    im = im.convert('RGB')
    if rotate:
        im = rotate_im(im)
    file_ending = im_file.split('.')[-1]
    im_pdf_outfile = im_file.replace(file_ending, 'pdf')
    im.save(im_pdf_outfile)
    tmp_pdfs.append(im_pdf_outfile)

# merge pdfs together
merger = PdfFileMerger()

for pdf in tmp_pdfs:
    merger.append(pdf)

merger.write(out_file)
merger.close()

# for pdf in tmp_pdfs:
#     os.remove(pdf)
