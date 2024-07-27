mylist = ['min', 'khant', 'han', 'lin', 'oo']
print(mylist)
mylist.remove('khant')
print(mylist)
mylist.pop(3) # remove with index number 
print(mylist)
print(mylist.index('lin')) 
mylist.clear()
# del mylist
print(mylist)

list2 = ['min', 'khant', 1, 1, 2]
count = list2.count(1)
print(f'1 in list2 is {count} time')

