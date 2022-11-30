n=int(input("enter the number="))
fact=0
for i in range(1,6,1):
    print(fact,"**",i,"=",fact)
    fact=fact+(i**3)
    print("factorial of n=",fact)
