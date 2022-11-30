def circle_impl(r):
    area=3.14*r**2
    perimeter=3.14*r*2
    return area,perimeter
r=int(input("enter the value="))
area,perimeter=circle_impl(r)
print("area=",area)
print("perimeter=",perimeter)
