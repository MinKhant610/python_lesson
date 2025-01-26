num = 10 

def myfun():
    global num
    num = 12
    print(num)

myfun()

def myfun2():
    print(num)

myfun2()

