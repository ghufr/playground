# timer_example.py

from time import time

def timer (func) :
    def f (x, y = 10):
        before = time()
        rv = func(x,y)
        after = time()
        print("elapsed ", after - before)
        return rv
    return f

@timer
def add(x,y=10):
    return x + y

@timer
def sub(x,y=10):
    return x - y

#Old Fashion way
# before = time()
print('add (10)', add(10))
# after = time()
# print(after - before)
print('add (20)', add(20))
print('sub (20)', sub(20))
