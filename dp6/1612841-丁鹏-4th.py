def add_log(level, _name=None, message=None):
    def decorate(func):
        def wrapper(*args):
            dict = {}
            dict['level'] = level
            dict['name'] = _name if _name else func.__module__
            dict['message'] = message if message else func.__name__
            print(func)
            func_log.append(dict)
        return wrapper
    return decorate


@add_log(0, 'add', 'add x and y')
def add(x, y):
    return x + y


@add_log(2)
def spam():
    print('Spam!')


func_log = list()
add(1, 2)
spam()
for i in func_log:
    print(i)
