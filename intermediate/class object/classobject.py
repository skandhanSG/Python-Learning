from object import employee

employees=[]

count = int(input("enter the count"))

for i in range(count):
    name = input("enter the name ")
    salary = int(input("enter the salary"))
    emp = employee(name,salary)
    employees.append(emp)

for emp in employees:
    emp.display()    