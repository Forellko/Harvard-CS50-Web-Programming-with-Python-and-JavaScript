def decorator(f):
    def wrapper():
        print('hello')
        f()
    return wrapper


@decorator
def func():
    print('world')


func()
