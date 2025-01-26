# reduce → ထည့်ပေးလိုက်တဲ့ iterables တွေကို fun(iter1, iter2) ဆိုပြီး param နှစ်ခုယူပြီး single value ရအောင်လုပ်

from functools import reduce 

list1 = [1, 2, 3, 4, 5]

my_redu = reduce(lambda num1, num2 :num1 + num2, list1)
print(my_redu)

my_range = reduce(lambda num1, num2: num1 + num2, range(5))
print(my_range)
