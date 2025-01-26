# partial → function တွေရဲ့ param တွေကို လျော့ချတဲ့ နေရာတွေမှာ သုံးနိုင်သလို ၊ ရှိပြီးသား function ကို argument တစ်ခုချိန်းပြီး fun အသစ်အဖြစ်လဲ အသုံး ပြုနိုင်ပါတယ်။

from functools import partial 

def power(base , exponent):
    return base ** exponent 

numbers = [1, 2, 3, 4]

square = partial(power, exponent=2)
squared_numbers = list(map(square, numbers)) 
print(squared_numbers)

two_power = partial(power, 2)
two_power_numbers = list(map(two_power, numbers))
print(two_power_numbers)
