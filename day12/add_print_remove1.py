def add(l):
    return(l)
l=["apple,banana,grapes,pineapple"]
while True:
    ch=int(input("enter the choice 1.add/n 2.print /n 3.remove /n 4.print /n 5.exit"))
    if ch==1:
        l.append("cherry")
        print(l)
    elif ch==2:
        print(l)
    elif ch==3:
        print(l.remove("cherry"))
    elif ch==4:
        print(l)
    else:
        break
