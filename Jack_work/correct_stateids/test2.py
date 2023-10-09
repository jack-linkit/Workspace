import re

pattern = r'\d+\. Warning: Student State ID provided.*'

string = '004138. Warning: Student State ID provided (6096804040) is different than the Student State ID currently associated with this student (20248157)'

if re.search(pattern, string):
    print(re.search(pattern, string))
else:
    print("No match.")