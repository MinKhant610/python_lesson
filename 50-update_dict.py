dict1 = {'name' : 'Min Khant', 'age' : 20}
print('Before Update ', dict1)
dict2 = {'age' : 21}

dict1.update(dict2)
print('After Update ', dict1)

dict3 = {'name' : 'Han Lin Oo', 'major' : 'mechatronics'}
dict1.update(dict3)
print(dict1)

dictA = {'a' : 1, 'b' : 2}
dictA.update([('a', 2), ('b', 3), ('c', 4)])
print(dictA)

dictB = {'age' : 5, 'd' : 6}
dictB.update(age=4, d=7)
print(dictB)

dictC = {'a' : 11, 'b' : 12}
dictC.update({'a' : 13, 'b':14, 'c' : 15})
print(dictC)

