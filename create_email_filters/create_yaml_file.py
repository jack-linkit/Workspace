import yaml
import csv

with open('madi.csv', 'r') as csv_file:
    csv_data = csv.reader(csv_file)
    data = [row for row in csv_data]

yaml_data = {'for_each': [], 'rule': {'label': "{label}", 'to': "*@{domain}"}}

for domain, label in data:
    label = label.lstrip()
    yaml_data['for_each'].append({'label': label, 'domain': domain})
    
yaml_data_2 = {'for_each': [], 'rule': {'label': "{label}", 'from': "*@{domain}"}}

for domain, label in data:
    label = label.lstrip()
    yaml_data_2['for_each'].append({'label': label, 'domain': domain})


# Writing the YAML data to a file
with open('to_filters.yaml', 'w') as file:
    yaml.dump(yaml_data, file)

with open('from_filters.yaml', 'w') as file:
    yaml.dump(yaml_data_2, file)