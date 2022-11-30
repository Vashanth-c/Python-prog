def perimeter_of_circle(r):
    perimeter=3.14*r*2
    return perimeter
def area_of_circle(r):
    area=3.14*r**2
    return area
r=int(input("enter r value="))
area=area_of_circle(r)
perimeter=perimeter_of_circle(r)
print("area=",area)
print("perimeter=",perimeter)
