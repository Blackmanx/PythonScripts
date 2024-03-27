import os
import sys
from tkinter import Tk, filedialog

def split_lines_into_files(file_path=None):
	if file_path is None:
		# If file path is not provided, prompt the user to select a file using a file manager
		root = Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()

	with open(file_path, 'r') as file:
		lines = file.readlines()

	file_name = os.path.basename(file_path)
	file_name_without_extension = os.path.splitext(file_name)[0]
	file_directory = os.path.dirname(file_path)

	for line_number, line in enumerate(lines, start=1):
		# Create a new file with the same name as the original file plus an underscore and the line number
		new_file_path = os.path.join(file_directory, f"{file_name_without_extension}_{line_number}.txt")
		with open(new_file_path, 'w') as new_file:
			new_file.write(line)

		print(f"Split line {line_number} into {new_file_path}")

# Check if file path is provided as an argument
if len(sys.argv) > 1:
	file_path = sys.argv[1]
	split_lines_into_files(file_path)
else:
	split_lines_into_files()
