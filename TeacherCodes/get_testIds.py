### open the file new.json and get all the testIds
import json
import re
import os
import sys
import csv


def get_testIds(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        testIds = []
        for i in data:
            testIds.append(i['testId'])
        return testIds
    

testIds = get_testIds('new.json')
for i in testIds:
    print(i, end=', ')
print()