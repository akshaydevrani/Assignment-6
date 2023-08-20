# Assignment-6
Assignment-6: JSON and OOP Assignment
Assignment 1
1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.
👉 Firstly we will create a JSON file named employee.json with the following content:
{
  "employees": [
    {
      "Name": "Ajeet Singh",
      "DOB": "1988-07-21",
      "Height": 165,
      "City": "New Delhi",
      "State": "Delhi"
    },
    {
      "Name": "Sambhav Suresh",
      "DOB": "1985-10-22",
      "Height": 170,
      "City": "Patna",
      "State": "Bihar"
    },
    {
      "Name": "Santosh Sinha",
      "DOB": "1992-03-10",
      "Height": 170,
      "City": "Gurgaon",
      "State": "Haryana"
    },
    {
      "Name": "Eram Javed",
      "DOB": "1988-11-02",
      "Height": 160,
      "City": "New Delhi",
      "State": "Delhi"
    },
    {
      "Name": "Daniel Haokip",
      "DOB": "1995-07-18",
      "Height": 180,
      "City": "Imphal",
      "State": "Manipur"
    }
  ]
}
👉Now we will create a Python program named employee_reader.py to read and process the JSON file:
import json
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
if _ _name__ == "_ _main__":
    main()



👉To run the employee_reader.py program and read the information from employee.json, we need to follow the below steps:
1.Place both the employee.json file and the employee_reader.py file in the same directory.
2.Open a terminal or command prompt.
3.Navigate to the directory where the files are located.
4.Once we are in the correct directory, we can run the Python script by entering the following command: python employee_reader.py
