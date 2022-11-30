def Hello(s):
    return s.lower()
print(Hello("This is Decorator"))
world=Hello
print(world("This is Decorator"))
def greet(func):
    print(func("This is Decor with arguments"))
greet(Hello)
greet(world)
def create_add(x):
    def add(y):
        print("y=",y)
        return x+y
    return add
z=create_add(10)
print(z(20))
