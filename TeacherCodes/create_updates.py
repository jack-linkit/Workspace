import re

def process_data_file(file_path, districtID):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # Initialize an empty list to store the SQL queries
            queries = []
            missing = []

            # Iterate through the lines in the file
            for line in lines:
                pattern = r'\(([^)]+)\)'
                match = re.findall(pattern, line)
                query_type = line[17:]
                if query_type.startswith('TeacherCode'):
                    query_type = 'Code'
                elif query_type.startswith('TeacherName'):
                    query_type = 'UserName'
                # Check if the line starts with "Line #"
                if len(match) == 3:
                    # If we have collected previous data, process it
                    query = None
                    if query_type == 'Code':
                        query = generate_sql_query(districtID, match[0], match[2], query_type)
                    elif query_type == 'UserName':
                        query = generate_sql_query(districtID, match[2], match[0], query_type)
                    if query and query not in queries:
                        queries.append(query)
                else:
                    # pattern = r'\d+\.\s+Warning:\s+Invalid\s+Program\s+(\w+)'
                    # match = re.search(pattern, line)
                    # if match:
                    #     new_query = f"INSERT INTO Program ([Name], DistrictID, AccessLevelID, Code, CreatedDate, ModifiedDate) VALUES ('{match.group(1)}', {districtID}, 4, '{match.group(1)}', GETDATE(), GETDATE());"
                    #     if new_query not in queries:
                    #         queries.append(new_query)
                    pattern = r'\d+\.\s+Warning:\s+Invalid\s+Student\sRace\s+(.*?)$'
                    match = re.search(pattern, line)
                    if match:
                        new_query = f"INSERT INTO Race ([Name], DistrictID, Code) VALUES ('{match.group(1)}', {districtID}, '{match.group(1)}');"
                        if new_query not in queries:
                            queries.append(new_query)


            return queries

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    
def generate_sql_query(districtID, teacher_code, teacher_name, query_type):
    # Split the line data into relevant parts
    
    # Generate the SQL query
    if query_type == 'Code':
        query = f"UPDATE [User] SET UserName = '{teacher_name}' WHERE DistrictID = {districtID} AND Code = '{teacher_code}';"
    elif query_type == 'UserName':
        query = f"UPDATE [User] SET Code = '{teacher_code}' WHERE DistrictID = {districtID} AND UserName = '{teacher_name}';"
    
    return query


# Example usage:
file_path = 'log.txt'
queries = process_data_file(file_path, 3856)

# Print the generated SQL queries
for query in queries:
    print(query)


