def gen_func():
    yield 10
    print("continue...")
    yield 20

    yield 30

for i in gen_func():
    print(i)
    
my_iter=iter(gen_func())
print(my_iter.__next__())
