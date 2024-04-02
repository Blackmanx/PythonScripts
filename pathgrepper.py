import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog

def execute_grep(folder_path, search_string):
    command = f"grep -ilr {search_string} {folder_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, errors="replace")
    output = result.stdout.strip()
    if output:
        # Split the output by newline character
        files = output.split('\n')
        # Get the relative path of each file
        relative_paths = [os.path.relpath(file, folder_path) for file in files]
        # Remove duplicate paths
        unique_paths = list(set(relative_paths))
        # Sort the paths alphabetically
        sorted_paths = sorted(unique_paths)
        # Join the sorted paths with newline character
        output = '\n'.join(sorted_paths)
        # Write the output to a file called "output.txt"
        with open("output.txt", "w") as file:
            file.write(output)
        print(output)
    else:
        print("No matches found.")


if len(sys.argv) != 3:
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    search_string = input("Enter the search string: ")
else:
    folder_path = sys.argv[1]
    search_string = sys.argv[2]

execute_grep(folder_path, search_string)
