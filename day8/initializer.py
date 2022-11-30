class employee:
    def __init__(self,name,employeeid,salary):
        self.name=name
        self.employeeid=employeeid
        self.salary=salary
    def get_details(self):
        print("name=",self.name)
        print("employeeid=",self.employeeid)
        print("salary=",self.salary)
    def get_bonus(self):
        return self.salary*0.25
name=input("enter the name=")
employeeid=int(input("enter the employeeid="))
salary=float(input("enter the salary="))
emp=employee(name,employeeid,salary)
emp.get_details()
if emp.salary>=12000.00:
    print("bonus=",emp.get_bonus())
else:
    print("no bonus")

# below line will check the program wheather class and object are connected   
# print(isinstance(emp,employee))
