import sys

def find_common_strings(file1_path, file2_path, output_path):
	with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as output_file:
		strings_file1 = set(file1.read().splitlines())
		strings_file2 = set(file2.read().splitlines())
		common_strings = sorted(strings_file1.intersection(strings_file2))
		output_file.write('\n'.join(common_strings))

# Usage example
if len(sys.argv) != 3:
	print("Usage: python remove.py <file1_path> <file2_path>")
	sys.exit(1)

file1_path = sys.argv[1]
file2_path = sys.argv[2]
output_path = input("Enter the output path: ")
find_common_strings(file1_path, file2_path, output_path)
