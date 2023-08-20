#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def main():
    employee_list = []

    with open('employee.json') as json_file:
        data = json.load(json_file)
        employees_data = data['employees']

        for emp_data in employees_data:
            employee = Employee(emp_data['Name'], emp_data['DOB'], emp_data['Height'], emp_data['City'], emp_data['State'])
            employee_list.append(employee)

    for emp in employee_list:
        print(f"Name: {emp.name}")
        print(f"DOB: {emp.dob}")
        print(f"Height: {emp.height}")
        print(f"City: {emp.city}")
        print(f"State: {emp.state}")
        print()

if __name__ == "__main__":
    main()

