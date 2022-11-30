nums=[10,12,13,9,6,25,12,15,16,19]
print("nums=",nums)
print("len(nums)=",len(nums))
output=list(filter(lambda a:a>=12,nums))
print("output=",output)
print("len(output)=",len(output))

def func(x):
    return x>=15
nums=[10,12,13,9,6,25,12,15,16,19]
print("nums=",nums)
print("len(nums)=",len(nums))
output=list(filter(func,nums))
print("output=",output)
print("len(output)=",len(output))


