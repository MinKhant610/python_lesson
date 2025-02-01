def div(x, y):
    print(x/y)

div(5, 10)

def working(fun):
    def wrapper(x, y):
        if x < y:
            x, y = y, x
        fun(x, y)
    return wrapper 

result = working(div)
result(5, 10)

