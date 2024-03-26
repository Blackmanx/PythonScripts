import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog
import argparse

def fuse_pdfs(folder_path, output_path):
	merger = PdfMerger()

	# Iterate over all files in the folder
	for filename in os.listdir(folder_path):
		if filename.endswith(".pdf"):
			file_path = os.path.join(folder_path, filename)

			# Add the PDF to the merger
			merger.append(file_path)

	# Write the fused PDF to the output path
	merger.write(output_path)
	merger.close()

# Create an argument parser
parser = argparse.ArgumentParser(description='Fuse multiple PDFs into one.')

# Add the folder path argument
parser.add_argument('--folder', type=str, help='Path to the folder containing PDFs')

# Add the output path argument
parser.add_argument('--output', type=str, help='Path to the output PDF')

# Parse the arguments
args = parser.parse_args()

# If folder path is provided as an argument, use it. Otherwise, ask the user to select the folder path using a file manager
if args.folder:
	folder_path = args.folder
else:
	root = tk.Tk()
	root.withdraw()

	# Ask for the folder path
	folder_path = filedialog.askdirectory(title="Select Folder")

# If output path is provided as an argument, use it. Otherwise, ask the user to select the output path using a file manager
if args.output:
	output_path = args.output
else:
	root = tk.Tk()
	root.withdraw()

	# Ask for the output path
	output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save Output PDF")

# Call the function to fuse the PDFs
fuse_pdfs(folder_path, output_path)
