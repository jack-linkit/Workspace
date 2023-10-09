import csv

# teacher_names = set()

# with open('CaseloadsImport 23-24.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         focus_group_name = row['Focus Group Name']
#         teacher_name = focus_group_name.split('23-24')[1].split('Caseload')[0].strip()
#         teacher_names.add(teacher_name)

# with open('teacher_names.txt', 'w') as f:
#     for teacher_name in teacher_names:
#         f.write(teacher_name.split('_')[0] + '\n')
#         print(f"SELECT '{teacher_name.split('_')[0]}', * FROM [User] with (nolock) WHERE DistrictID = 4877 AND FullName LIKE '%{teacher_name}%'")

classes = {}

with open('CaseloadsImport 23-24.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        teacher_name = row['Focus Group Name'].split('23-24')[1].split('Caseload')[0].strip().split('_')[0]
        class_name = row['Focus Group Name']
        student_id = row['Student ID']
        if class_name not in classes:
            classes[class_name] = {'teacher': teacher_name, 'students': [student_id]}
        else:
            classes[class_name]['students'].append(student_id)

teacher_id_school = {}
# open and read the tab delimited file matches.txt
with open('matches.txt') as f:
    matches = f.read().splitlines()
    for match in matches:
        data = match.split('\t')
        teacher_name = data[0]
        userID = data[1]
        schoolID = data[2]
        teacher_id_school[teacher_name] = [userID, schoolID]

with open('query.txt', 'w') as f:
    districtID = 4877
    districtTermID = 119128
    my_userID = 4940734
    f.write('INSERT INTO Class ([Name], Locked, SchoolID, DistrictTermID, UserID, DistrictID, ClassTypeID, CreatedDate, ModifiedDate, MOdifiedUser, ModifiedBy) VALUES \n')
    for class_name, data in classes.items():
        teacher = data['teacher']
        students = data['students']
        if teacher_id_school.get(teacher):
            teacher_id = teacher_id_school[teacher][0]
            school_id = teacher_id_school[teacher][1]
        else:
            teacher_id = 1033148 # Ian Carder's ID
            school_id = 0
        if int(school_id) == 0:
            school_id = 'NULL'
        f.write(f'(\'{class_name}\', 0, {school_id}, {districtTermID}, {teacher_id}, {districtID}, 2, GETDATE(), GETDATE(), {my_userID}, {my_userID}),\n')

class_dict = {}

with open('class_ids.txt', 'r') as f:
    for line in f.read().splitlines():
        class_id, class_name = line.strip().split('\t')
        class_dict[class_name] = class_id


student_dict = {}

with open('students.txt', 'r') as f:
    for line in f.read().splitlines():
        code, student_id = line.strip().split('\t')
        student_dict[code] = student_id

with open('query2.txt', 'w') as f:
    f.write('INSERT INTO ClassStudent (ClassID, StudentID, Active) VALUES \n')
    counter = 0
    for class_name, data in classes.items():
        students = data['students']
        class_id = class_dict[class_name]
        for student in students:
            try:
                student_id = student_dict[student]
            except KeyError:
                counter += 1
                print(student)
                continue
            f.write(f'({class_id}, {student_id}, 1),\n')

print(counter)



