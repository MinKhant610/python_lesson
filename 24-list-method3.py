mylist = ['min', 1, 2, 3]
print(mylist)
mylist.insert(1, 'khant')
print(mylist)
mylist.reverse()
print(mylist)
mylist[0:4] = mylist[0:4][::-1] #reverse index 1 to 3 only
print(mylist)

newlist = [4, 2, 3, 9, 0]
newlist.sort()
print(newlist)
# 5 6 9 => 9 6 5
list2 = ['apple', 'pineapple', 'banana']
list2.sort(key=len, reverse=True)
print(list2)

string1 = 'apple'
string2 = 'apple'
string3 = string1 is string2
print(string3)
print(id(string1), id(string2))

newlist1 = ['apple']
newlist2 = ['apple']
newlist3 = newlist1 is newlist2
print(newlist3) 
print(id(newlist1), id(newlist2))
