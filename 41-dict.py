dict1 = {} 
print(dict1)
print(type(dict1))

dict1[10] = 'Min Khant'
dict1[20] = 'Han Lin Oo'
dict1[30] = 'Zin Zin Win Htet'

print(dict1)

dict2 = {'name': 'Min Khant', 'roll':17, 'major':'Mechatronics'}
print(dict2.keys())
print(dict2.values())
print(dict2['roll'])

for key, value in dict2.items():
    print(key, value)

