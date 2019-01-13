def bold(funkcja):
    def wrapper(*args,**kwargs):
        return f"\<b>{funcja(*args,*kwargs}</b>)"
    return wrapper

def italic(funkcja):
    pass

@bold
#@italic
def foo(arg):
    return f"to jest{arg}"