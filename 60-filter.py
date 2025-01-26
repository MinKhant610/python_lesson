# filter → iter ကို fun ထဲဖြတ်စေပြီး True ဖြစ်တဲ့ကောင်တွေကို return ပြန်ပေး

def checkEven(num):
    if num%2 == 0:
        return True 
    else:
        return False 

list_ = [0, 6 , 7, 9, 12, 18]
even_list = list(filter(checkEven, list_))
print(even_list)

# Write a program to distinguish even and odd numbers from the input list by
# using the filter() and lambda function.

checkEvenLam = list(filter(lambda num:num%2 == 0, list_))
print(checkEvenLam)

