f=open("hello.txt","r")
data=f.read()
print(data)
print("\n")
f.close()

f=open("hello.txt","r")
print(f.readline())
print(f.readline())
print("\n")

f=open("hello.txt","r")
l=f.readlines()
print(l)
print("\n")

f=open("hello.txt","r")
while True:
    data=f.read(10)
    print(data)
    if not data:
        break
