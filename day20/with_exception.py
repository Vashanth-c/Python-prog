a,b=10,0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print ("Don\'t use b as zero")
finally:
    print("always executed")
print("welcome")
