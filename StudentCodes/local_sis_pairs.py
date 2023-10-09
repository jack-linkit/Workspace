import csv

with open('STUDENTS.txt', 'r') as infile:
    # open with dictreader
    with open('query.txt', 'w') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')
        outfile.write('DECLARE @LocalSISPairs TABLE (SIS_ID INT, LOCAL_ID INT);\n')
        outfile.write('INSERT INTO @LocalSISPairs (SIS_ID, LOCAL_ID) VALUES ')
        row_count = 0
        for row in reader:
            if row_count > 100:
                outfile.write('\n')
                outfile.write('INSERT INTO @LocalSISPairs (SIS_ID, LOCAL_ID) VALUES ')
                row_count = 0
            else:
                outfile.write(', \n')
            sis_id = row['ID']
            local_id = row['STUDENT_NUMBER']
            outfile.write(f'({sis_id}, \'{local_id}\')')
            row_count += 1

        
