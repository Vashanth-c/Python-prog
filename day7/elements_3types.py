class employee:
    name=" "
    employeeid=0
    salary=0.0
    def get_details(self):
        print("name=",self.name)
        print("employeeid=",self.employeeid)
        print("salary=",self.salary)
    def get_bonus(self):
        return self.salary*0.25
emp=employee()
print("before calling:")
emp.name=input("enter the name=")
emp.employeeid=int(input("enter the employeeid="))
emp.salary=float(input("enter the salary="))
emp.get_details()
if emp.salary>=12000.00:
    print("bonus=",emp.get_bonus())
else:
    print("no bonus")
    
