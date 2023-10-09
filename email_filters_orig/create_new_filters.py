import yaml
import csv


with open('data.csv', 'r') as csv_file:
    data = csv.reader(csv_file)

yaml_data = {'for_each': [], 'rule': {'label': "{label}", 'to': "{domain}"}}

for domain, label in data.items():
    yaml_data['for_each'].append({'label': label, 'domain': domain})

# Writing the YAML data to a file
with open('output.yaml', 'w') as file:
    yaml.dump(yaml_data, file)
