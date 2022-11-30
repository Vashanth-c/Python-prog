students={}
def add_marks():
    sub_marks=()
    m1=int(input("enter the m1 value="))
    m2=int(input("enter the m2 value="))
    sub_marks['tamil']=m1
    sub_marks['english']=m2
    sub_marks['total']=m1+m2
    print(sub_marks)
    return sub_marks
def add_students():
    name=input("enter the name=")
    student[name]=add_marks()
    print(student)
def remove(stu):
    del student[stu]
def select_all():
    print("NAME\tTAMIL\tENGLISH\tTOTAL")
    print("------------------------")
    for i,j in student.items():
        print(i,end="\t")
        for m,n in j.items():
            print(n,end="\t")
        print()

while True:
    ch=int(input("enter the choice:\n1.add\n2.select_all\n3.remove"))
    if ch==1:
        add_students()
    elif ch==2:
        select_all()
    elif ch==3:
        stu=input("enter student name=")
        remove(stu)
    else:
        break
