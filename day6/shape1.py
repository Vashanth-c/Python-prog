from shape import circle
while True:
    ch=int(input("enter the option 1.rectangle ,\n 2.square ,\n 3.circle ,\n 4.exit"))
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
    print("break")
