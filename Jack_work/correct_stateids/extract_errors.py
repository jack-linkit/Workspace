import re
import sys

def extract_warning_lines(filename):
    pattern = r'\d+\. Warning: Student State ID provided.*'

    with open(filename, 'r') as file:
        lines = file.readlines()

    matching_lines = [line.strip() for line in lines if re.match(pattern, line)]
    return matching_lines

filename = 'log.txt'  # Replace with the actual path to your input file
warning_lines = extract_warning_lines(filename)

print(len(warning_lines), file=sys.stderr)
for line in warning_lines:
    print(line)
