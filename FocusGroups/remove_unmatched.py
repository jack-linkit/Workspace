names = ['Boykin','Brunner','Charles','Chylack','Cusic','Fay','Garber','Hanssens','Wieczorek','Hediger','Howard','Hutchings','Lauer','Lintner','Muller','Paul','Peterson','Pinder','Pollock','Power','Raffin','Stevens','Stokes','White']


names_set = set(names)

with open('teacher_names.txt', 'r') as f:
    teacher_names = f.read().splitlines()
    with open('teacher_names_matched.txt', 'w') as f2:
        for teacher_name in teacher_names:
            if teacher_name not in names_set:
                f2.write(teacher_name + '\n')
