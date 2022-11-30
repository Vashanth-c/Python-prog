def add(l,s):
    return(l+s)
l=["apple,banana,grapes,pineapple"]
while True:
    ch=int(input("enter the choice 1.add/n 2.print /n 3.remove /n 4.exit /t"))
    if ch==1:
        s=",cherry"
        L=l+s
        print(L)
    elif ch==2:
        print(L)
    elif ch==3:
        print(l.remove["grapes"])
        print(l)
    else:
        break
    

