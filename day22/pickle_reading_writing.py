class student:
    Name="   "
    Age=0
    def get_details(self):
        print(self.Name)
        print(self.Age)
s=student()
s.Name="vashanth"
s.Age=22
#s.get_details()

import pickle
f=open("D:\\python program\\day22\\oops.dat","wb")
pickle.dump(s,f)
f.flush()
f.close()

import pickle
f=open("D:\\python program\\day22\\oops.dat","rb")
s1=pickle.load(f)
s1.get_details()
f.close()
