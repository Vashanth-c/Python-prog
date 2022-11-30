mark=int(input("enter the mark= "))
if mark>=36:
    if mark>=90:
        print("O grade")
    elif mark>=80:
        print("A+ grade")
    elif mark>=70:
        print("A grade")
    elif mark>=60:
        print("B+ grade")
    elif mark>=50:
        print("B grade")
else:
    print("you are fail")
