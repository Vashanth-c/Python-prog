def rectangle(l,b):
    return l,b
def square(a):
    return a*a
def circle (r):
    return 3.14*r**2
temp=1
while temp>=1:
    ch=int(input("enter the option \n 1.rectangle \n 2.square \n 3.circle \n 4.exit \n"))
    if ch==1:
        l=int(input("enter the length="))
        b=int(input("enter the breath="))
        area=rectangle(l,b)
        print("area of rectangle=",area)
    elif ch==2:
        a=int(input("enter the side="))
        area=square(a)
        print("area of square=",area)
    elif ch==3:
        r=int(input("enter the radius="))
        area=circle(r)
        print("area of circle=",area)
    else:
        break
    
