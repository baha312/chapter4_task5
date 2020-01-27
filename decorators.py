from datetime import datetime

# -----------------decorators------------

def time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func()
        result = datetime.now()
        return result
    return wrapper

@time

def func_one(num):
    new_list = [x for x in range(1,num)]
    return new_list

@time

def func_two(num):
    new_list = []
    for x in range(1,num):
        new_list.append(x)
    return new_list

print(func_one(1000000))
print(func_two(1000000) )
