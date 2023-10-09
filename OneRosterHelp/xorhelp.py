import csv

xor_rows = []
with open("new_districtTerms.csv", "r") as newtermsfile:
    csvreader = csv.reader(newtermsfile)
    next(csvreader)
    for row in csvreader:
        districtTermID = row[0]
        districtID = int(row[2])
        TermSourceIDs = row[5].split('|')
        termSourceIds_str = ','.join(TermSourceIDs)
        DistrictTermName = row[1]
        xor_rows.append([termSourceIds_str, districtTermID, DistrictTermName, districtID])

with open("new_xors.csv", "w") as outfile:
    csvwriter = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in xor_rows:
        csvwriter.writerow(row)
        print(f"('{row[0]}', {row[1]}, '{row[2]}', {row[3]})", end=",")
    print()
        