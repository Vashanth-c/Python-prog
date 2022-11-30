try:
    a=int(input("enter a="))
    b=int(input("enter b="))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Don\'t use b as zero")
except ValueError:
    print("use only digits")
except Exception:
    print("others")

