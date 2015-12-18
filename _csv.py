# coding=utf-8

import csv
import collections

EmployeeRecord = collections.namedtuple('EmployeeRecord', 'name, age, title, department, paygrade, df, sdf')

for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print emp.name, emp.title, emp.age