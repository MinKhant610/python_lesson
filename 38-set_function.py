set1 = {1, 2, 4, 5}
print(set1)

# add function
set1.add(6)
print(set1)
set1.add(0)
print(set1)
set1.add(3)
print(set1)

# update 
list1 = [7, 3, 11 , 2]
set2 = {1 ,2, 3, 4, 5}

set2.update(list1, set2)
print(set2)


#copy 
print('set 1 ', set1)
set3 = set1.copy()
print('set 3 ', set3)

#pop
set4 = {4, 1, 3, 2} # => 1 2 3 4 
print(set4.pop()) # ဖျက်သွားတဲ့ element ကိုပြ
print(set4)

#remove 
set5 = {4, 1, 3, 2}
print('set 5 ', set5)
set5.remove(3)

#discard ကမရှိတဲ့ ကောင်ကိုဖျက်လဲ error မတက်ဘူး
set6 = {1, 2, 3, 4, 5 , 6}
print('set 6 ', set6)
set6.discard(1)
print('set 6 ', set6)
set6.discard(7)
print('set 6 ', set6)

set6.clear()
print('set 6 ', set6)