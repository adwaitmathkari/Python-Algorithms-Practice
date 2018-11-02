
def foo(n):
    if n == 2:
        raise ValueError("double trouble")
    elif n == 1:
        raise ValueError("single wiggle")
    else: 
        print("OK")


def bar(n):
    try:
        foo(n)
    except ValueError as e:
        print("the error message is '%s'" % str(e))