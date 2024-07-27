mylist = ['min', 'khant', 1, 2, 3]
print(mylist)
mylist.append('zin zin win htet')
print(mylist)
newlist = ['han', 'lin', 'oo']
mylist.append(newlist)
print(mylist)
list2 = ['myat', 'thu']
mylist.extend(list2)
print(mylist)
list3 = ['bhone', 'thant']
mylist += list3 # same as extend 
print(mylist)

