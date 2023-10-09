import csv

# read in the first column of CaseloadsImport 23-24.csv and output to students.txt
with open('CaseloadsImport 23-24.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('students.txt', 'w') as f:
        for row in reader:
            f.write(row['Student ID'] + '\n')