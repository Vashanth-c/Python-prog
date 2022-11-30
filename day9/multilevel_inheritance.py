class employee:
    def set_details(self,name,emid,sal):
        self.name=name
        self.emid=emid
        self.sal=sal
    def get_details(self):
        print("name=",self.name)
        print("emid=",self.emid)
        print("sal=",self.sal)
class pf(employee):
    def get_pf(self):
        self.sal=sal
        return self.sal*0.12
class bonus (pf):
    def get_bonus(self):
        return self.sal*0.25
emp=bonus()
name=input("enter the name=")
emid=int(input("enter the emid="))
sal=float(input("enter the sal="))
emp.set_details(name,emid,sal)
emp.get_details()
if emp.sal>=12000.00:
    print("bonus=",emp.get_bonus())
else:
    print("no bonus")
print("pf=",emp.get_pf())
        
