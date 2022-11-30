s=input("enter the password=")
u,sp,n=0,0,0
for i in range(0,len(s)):
    if s[i].isupper():
        u=u+1
    elif s[i].isdigit():
        n=n+1
    elif s[i]=="$" or s[i]=="@"or s[i]=="*":
        sp=sp+1
    else:
        pass
if u>=1 and n>=1 and sp==1:
    print("valid password")
else:
    print("not valid")
