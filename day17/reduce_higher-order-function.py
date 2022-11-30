from functools import reduce
nums=[1,2,3,4,5]
print("nums=",nums)
output=reduce(lambda a,b:(a,b),nums)
print("output=",output)

from functools import reduce
def func(a,b):
    return a+b
nums=[1,2,3,4,5]
print("nums=",nums)
output=reduce(func,nums)
print("output=",output)
