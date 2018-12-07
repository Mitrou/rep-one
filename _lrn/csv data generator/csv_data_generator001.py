import csv
from random import choice
import random

# set choice data. more is better for bigger versatility
FIRST_NAMES = ('john', 'bob', 'sara', 'phenix', 'jordan', 'henry')
LAST_NAMES = ('benin', 'rosman', 'krudo', 'shemlin', 'lord', 'sams')
SENIORITY = ('junior', 'middle', 'senior', 'lead', 'guru')
POSITIONS = ('tester', 'automation', 'developer', 'admin')
CRT_FLG = ('Y', 'N')

# generation csv file
with open('csvfile.csv', 'w') as csvOutput:
    testData = csv.writer(csvOutput, delimiter=',', escapechar=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL,
                          lineterminator='\n')
    # set header
    testData.writerow(['fName lName'] + ['Seniority'] + ['Position'] + ['Salary'] + ['KPI'] + ['critFlag'])
    for i in range(1, 800):
        random_name = "{} {}".format(choice(FIRST_NAMES), choice(LAST_NAMES))
        testData.writerow([random_name] + [choice(SENIORITY)] + [choice(POSITIONS)] +
                          [random.randrange(30000, 120000, 1000)] + [random.random()] + [choice(CRT_FLG)])
