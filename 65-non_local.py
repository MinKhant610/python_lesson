# global variable လို လည်း တခြား ကောင်တွေက ခေါ်သုံးတာ မခံခြင်ဘူး Nested Function ထဲမှာလည်း variable ကိုပြင်လို့ရခြင်တယ်ဆို nolocal ဆိုတဲ့ ကောင်ကိုသုံးလို့ရတယ်။ 

#Nested Function
def fun1():
    name = 'Maung Maung'
    def fun2():
        name = 'Aung Aung'
        print(name)
    fun2()
    print(name)
fun1()

#using non local
def fun1():
    name = 'Maung Maung'
    def fun2():
        nonlocal name 
        name = 'Aung Aung'
        print(name)
    fun2() 
    print(name)
fun1()