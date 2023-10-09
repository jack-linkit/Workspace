class_dict = {}

with open('class_ids.txt', 'r') as f:
    for line in f:
        class_id, class_name = line.strip().split('\t')
        class_dict[class_name] = class_id


