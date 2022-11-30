import pickle
l=[100,"hello",10.5]
f=open("D:\\python program\\day22\\objex.dat","wb")
pickle.dump(l,f)
f.flush()
f.close()
