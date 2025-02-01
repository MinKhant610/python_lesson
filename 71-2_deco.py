def fun1(fun):
    def wrapper():
        print('Hello I am fun 1')
        fun()
    return wrapper

def fun2(fun):
    def wrapper():
        print('Hello I am fun 2')
        fun()
    return wrapper


@fun1
@fun2
def hello():
    print('Hello')

hello()