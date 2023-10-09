import re

pattern = r'\d+\.\sWarning:\sStudent\sState\sID\sprovided\s\(\d+\)\sis\sdifferent\s than\s the\s Student\s State\s ID\s currently\s associated\s with\s this\s student\s\(\d+\)'


string = '004138. Warning: Student State ID provided (6096804040) is different than the Student State ID currently associated with this student (20248157)'

print(re.match(pattern, string))