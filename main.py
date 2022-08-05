from PyPDF2 import PdfMerger
import os

# PDF folder
pdfs_folder = "./pdfs/"
# Merged pdfs folder
merged_folder = "./merged/"
# PDF merger
merger = PdfMerger()

def merge():
    '''Get all the pdf files from one folder and merge them into a single file before saving them to another folder'''
    # Loop through pdf files in a folder
    for file in os.listdir(pdfs_folder):
        if file.endswith(".pdf"):
            merger.append(pdfs_folder + file)
    
    merger.write(merged_folder + "combinedPDFs.pdf")
    merger.close()


if __name__=="__main__":
    merge()
