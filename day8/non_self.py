class employee:
    name=" "
    emid=0
    sal=0.0
    def get_details():
        print("name=",employee.name)
        print("emid=",employee.emid)
        print("sal=",employee.sal)
    def get_bonus(self):
        return employee.sal*0.25
emp=employee()
employee.name=input("enter the name=")
employee.emid=int(input("enter the emid="))
employee.sal=float(input("enter the sal="))
employee.get_details()
if emp.sal>=12000.00:
    print("bonus=",emp.get_bonus())
else:
    print("no bonus")
