import csv


with open('StudentMap.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f'({row["StudentID"]}, {row["WrongStudentID"]})', end=', ')