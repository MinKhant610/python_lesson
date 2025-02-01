# Closure ကို decorator function တွေမှာ အများဆုံး အသုံးပြုပါတယ်။ (Decorator ဆိုတာ မူရင်းရှိပြီးသား function or object တစ်ခုထဲကို လုပ်ဆောင်ချက် အသစ်ထပ်ထည့်လိုတဲ့အခါမှာသုံးပါတယ်။)

def simple_decorator(fun):
    def wrapper():
        print('function is beging called')
        fun()
        print('function has finished')
    return wrapper

@simple_decorator
def sayHello():
    print('Hi I am say hello')

sayHello()

