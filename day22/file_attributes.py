f=open("D:\\python program\\day21\\hellocopy.txt","r")
print("name=",f.name)
print("mode=",f.mode)
print("before closed",f.closed)
f.close()
print("after closed",f.closed)
