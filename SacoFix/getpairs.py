import csv 


stud_dict = {}

with open('dupstudents.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        fullname = row[1] + row[2]
        if fullname in stud_dict:
            if stud_dict[fullname][2] > int(row[3]):
                stud_dict[fullname][1] = row[0]
            else:
                stud_dict[fullname][1] = stud_dict[fullname][0]
                stud_dict[fullname][0] = row[0]
                stud_dict[fullname][2] = int(row[3])

        else:
            stud_dict[fullname] = [row[0], None, int(row[3])] 

for key in stud_dict:
    if stud_dict[key][1] is not None: 
        print(f'({stud_dict[key][0]}, {stud_dict[key][1]})', end=',')
