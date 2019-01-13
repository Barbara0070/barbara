import time
start=time.time()
lista=[x*2 for x in range(100000)]
stop=time.time()
print(stop-start)
def log(funkcja):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=funkcja(*args,**kwargs)
        stop=time.time()
        duration=stop-start
        print(f"dlugosc wywolania {funkcja.__name__} to {duration} s")
        return result
    return wrapper
def foo(bar):
    print(bar.__name__)
foo(print)
@log
def foo(arg):
    return f"to jest {arg}"



foo('1')