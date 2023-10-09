import csv

with open('dumbteachers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(f'(\'{row[0]}\', \'{row[1]}\')', end=',')
print()