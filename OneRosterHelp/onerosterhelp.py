import csv
import sys

inputfile = "academicSessions.csv"

if inputfile is None:
    raise ValueError("inputfile is required")

with open(inputfile, 'r') as infile:
    lines = csv.DictReader(infile)

    districtID = 3856 # set districtID here

    your_usedID = 4940734

    current_date = '2023-08-14'

    if districtID is None:
        raise ValueError("DistrictID required")


    # Initialize a dictionary to store the titles and sourceIds
    title_sourceIds = {}
    new_districtTerms = {}

    # Process the data
    for line in lines:
        if line:
            title = line['title']
            sourceId = line['sourcedId']
            dateStart = line['startDate']
            dateEnd = line['endDate']

            if title not in new_districtTerms:
                new_districtTerms[title] = [districtID, dateStart, dateEnd, []]

            new_districtTerms[title][3].append(sourceId)

# Write the CSV output to a file
output_filename = "districtTerms.csv"
with open(output_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(["Title", "DistrictID", "DateStart", "DateEnd", "SourceIds", "CreatedByUserID", "DateCreated"])
    for title in new_districtTerms:
        districtID, startDate, endDate, sourceIds = new_districtTerms[title]
        sourceIds_str = '|'.join(sourceIds)
        csvwriter.writerow([title, districtID, startDate, endDate, sourceIds_str, your_usedID, current_date])


output_filename2 = "XORDistrictTermMappings.csv"
with open(output_filename2, 'w') as xorfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(["TermSourceID", "DistrictTermID"])
    for title in new_districtTerms:
        districtID, startDate, endDate, sourceIds = new_districtTerms[title]
        sourceIds_str = ','.join(sourceIds)
        csvwriter.writerow([])


print(f"Data written to {output_filename}\n")

with open("output.csv", "r") as outfile:
    csvreader = csv.DictReader(outfile)
    for line in csvreader:
        print(f"('{line['Title']}', {line['DistrictID']}, '{line['DateStart']}', '{line['DateEnd']}', '{line['SourceIds']}', {line['CreatedByUserID']}, '{line['DateCreated']}')", end=", ")
    print()



