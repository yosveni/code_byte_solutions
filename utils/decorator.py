def debug(f):
    def new_func(a, b):
        print("Function add() called!")
        return f(a, b)
    return new_func


@debug
def add(a, b):
    return a + b


print(add(7, 5))