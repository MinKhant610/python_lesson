#Nested function 

def fun1():
    print('fun1() function start')
    def fun2():
        print('fun2 execution')
    print('fun1 calling to fun2')
    fun2() 

# fun1()

# function returning other function
def fun1():
    print('fun1() function start')
    def fun2():
        print('fun2 execution')
    print('fun1 return to fun2')
    return fun2

fun2 = fun1()
fun2()