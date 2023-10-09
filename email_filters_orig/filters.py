import xml.etree.ElementTree as ET
import json

def extract_email_filters(xml_file):
    email_filters = {}

    # Define the namespaces used in the XML
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'apps': 'http://schemas.google.com/apps/2006'
    }

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Use the proper namespace when searching for elements
    for entry in root.findall('.//atom:entry', namespaces=namespaces):
        from_property = entry.find(".//apps:property[@name='from']", namespaces=namespaces)
        label_property = entry.find(".//apps:property[@name='label']", namespaces=namespaces)

        if from_property is not None and label_property is not None:
            email_address = from_property.attrib['value']
            label = label_property.attrib['value']
            email_filters[email_address] = label

    return email_filters

# Replace 'path/to/your/xml_file.xml' with the actual path to your XML file.
xml_file_path = 'mailFilters.xml'
result = extract_email_filters(xml_file_path)

with open('dict.json', 'w') as json_file:
    json.dump(result, json_file)

