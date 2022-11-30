n=int(input("enter the number="))
fact=1
for i in range(1,16,2):
    print(fact,"+",i,"=",fact)
    fact=fact+i
else:
    print("factorial of n=",fact)
