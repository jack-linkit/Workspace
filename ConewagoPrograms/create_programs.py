import csv


code_dict = {}
with open('program_codes.txt', 'r') as f:
    for line in f:
        full_code = line 
        options = line.split('|')
        for opt in options:
            opt = opt.strip()
            code_dict[opt] = full_code.strip()


with open('student_roster.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)

    with open('student_programs.txt', 'w') as f:
        for row in reader:
            local_code = row[11]

            for program in row[20:]:
                if program in code_dict:
                    program = code_dict[program]
                
                if program != '':
                    f.write(local_code + '\t' + program + '\n')


    