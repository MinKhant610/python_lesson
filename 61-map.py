# map → ထည့်ပေးလိုက်တဲ့ iterables တစ်ခုခြင်းစီကို ရှေ့က function အတိုင်း လုပ်
list_ = [1, 11, 22, 33]

def myfun(num):
    return num*2 

mymap = list(map(myfun, list_))
print(mymap)

# Write a program using the lambda function that identifies the square of a
# number

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

multi_list = list(map(lambda list1, list2: list1 * list2, list1, list2))
print(multi_list)