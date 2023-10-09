import re
import csv

def extract_state_ids(file_path):
    state_ids = set()
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            match = re.search(r'\((\d+)\)', line)
            if match:
                state_id = match.group(1)
                state_ids.add(state_id)
    print(len(state_ids))
    return state_ids

def read_all_students(file_path):
    all_students = {}
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            SISID = row[0]
            stateID = row[17]
            print(SISID, stateID)
            all_students[stateID] = SISID
    print(len(all_students))
    return all_students

errors_path = 'errors.txt'
students_path = 'full_students.csv'
state_ids = extract_state_ids(errors_path)
all_students = read_all_students(students_path)

with open('out.csv', 'w') as outfile:
    csv_writer = csv.writer(outfile)
    with open('full_students.csv') as studentfile:
        students_reader = csv.reader(studentfile)
        for id in state_ids:
            csv_writer.writerow([all_students[id], id])
            

    
        
