import os
from PIL import Image
from PyPDF2 import PdfFileMerger

input_path = '/home/nick/Downloads'
im_files = [os.path.join(input_path, 's_1.jpeg'),
        os.path.join(input_path, 's_2.jpeg'),
        os.path.join(input_path, 's_3.jpeg')]
out_file = os.path.expanduser('~/Schadensfall.pdf')
out_dir = os.path.dirname(out_file)

tmp_pdfs = []

# convert images to pdf
for im_file in im_files:
    im = Image.open(im_file)
    im = im.convert('RGB')
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

for pdf in tmp_pdfs:
    os.remove(pdf)
