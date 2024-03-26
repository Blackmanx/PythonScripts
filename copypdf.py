import sys
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def copy_pdf(source_path, destination_path):
	# Open the source PDF file in read-binary mode
	with open(source_path, 'rb') as source_file:
		# Create a PDF reader object
		reader = PyPDF2.PdfReader(source_file)

		# Create a PDF writer object
		writer = PyPDF2.PdfWriter()

		# Open the destination PDF file in read-binary mode
		with open(destination_path, 'rb') as destination_file:
			# Load the existing PDF content into the writer object
			writer.append(fileobj=destination_file)

		# Iterate over each page in the source PDF
		for page_num in range(len(reader.pages)):
			# Get the page object
			page = reader.pages[page_num]

			# Add the page to the writer object
			writer.add_page(page)

		# Open the destination PDF file in write-binary mode
		with open(destination_path, 'wb') as destination_file:
			# Write the modified PDF to the destination file
			writer.write(destination_file)

	print("PDF pages copied successfully!")

if len(sys.argv) == 3:
	source_path = sys.argv[1]
	destination_path = sys.argv[2]
else:
	# Create a Tkinter root window
	root = tk.Tk()
	root.withdraw()

	# Prompt the user to select the source PDF file
	source_path = filedialog.askopenfilename(title="Select Source PDF File")

	# Prompt the user to select the destination PDF file
	destination_path = filedialog.asksaveasfilename(title="Select Destination PDF File", defaultextension=".pdf")

# Call the copy_pdf function with the selected paths
copy_pdf(source_path, destination_path)
