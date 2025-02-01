# Closure ကို global variable တွေမသုံးဘဲ non local နဲ့ state တစ်ခုကို ထိန်းထားခြင်တဲ့အခါတွေမှာ သုံးလို့ရတယ် သူက function delete ခံလိုက်ရရင်တောင် data value ကိုမှတ်ပြီးသိမ်းပေးထားနိုင်တယ် 

# Closure function တစ်ခုဖြစ်ဖို့ဆို 

# 1. Nested Function တစ်ခုဖြစ်ရမယ်
# 2. Nested Function ထဲမှာ variable ကို သူ့အပြင်ဘက်မှာကြော်ငြာထားရမယ် 
#     1. outer function က variable ကို inner function ထဲမှာပြန်သုံးရမယ်
# 3. Enclosing or Outer Function က Nested Function (inner function) ကို return ပြန်ပေးရမယ်

def fun1():
    data = 'I belong to fun1'
    def fun2():
        print(data)
    return fun2 

obj = fun1() 
del fun1
obj() 

