import colorama

def first_function():
    pass


class Human:
    pass

rq = colorama
first_f = first_function()
nick = Human
try:
    print(colorama.__name__)
    print(rq.__name__)
    print(first_function.__name__)
    print(first_f.__name__)
    print(Human.__name__)
    print(nick.__name__)
    print("--------------------------")
except:
    my_int = 0
    my_fl = 0.1
    my_str = 'hi'
    my_b = True
print(type(my_int))
print(type(my_fl))
print(type(my_str))
print(type(my_b))
print(type(colorama))
print(type(rq))
print(type(first_function))
print(type(first_f))
print(type(Human))
print(type(nick))
print("--------------------------")
my_list = []
for method in dir(my_list):
    print(method)
print("--------------------------")
data = 'string'
print(hasattr(data, 'reverse'))
print(hasattr(data, 'index'))

print(getattr(data, 'startswith'))
print(getattr(data, 'startswith', None))
print(getattr(data, 'reverse', None))
print("--------------------------")

data = 'string'
def func():
    pass

print(callable(data))
print(callable(func))
print("--------------------------")

