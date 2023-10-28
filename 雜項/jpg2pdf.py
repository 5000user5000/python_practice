# convert many jpgs into a single pdf
import os
import img2pdf
import numpy as np

#remember to "pip install img2pdf"

# Replace the directory path with the folder containing JPEG images to be converted
directory_path = "D:/img"

# List all files in the directory and filter only JPEG images (ending with ".jpg")
image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]
image_files.sort(key=lambda x: int(x[:-4])) #  sort file by filename number (1.jpg、2.jpg)       # detail: https://blog.csdn.net/qq_36481821/article/details/83214167

# Convert the list of JPEG images to a single PDF file
pdf_data = img2pdf.convert([os.path.join(directory_path, img).encode() for img in image_files])

# Write the PDF content to a file (make sure you have write permissions for the specified file)
with open("output.pdf", "wb") as file:
    file.write(pdf_data)
