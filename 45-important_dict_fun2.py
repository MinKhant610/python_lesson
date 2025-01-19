data = {1:'Min Khant', 3:'Zin Zin Win Htet', 2:'Han Lin Oo'}
print(data)

print(data.popitem())
print(data)

# data2 = {}
# print(data2.popitem())

data3 = {'name': 'Min Khant', 'age': 20, 'school':'TU'}

#get only keys
for key in data3.keys():
    print(key)

#get only values
for value in data3.values():
    print(value)

#get keys and values 
for key, value in data3.items():
    print(key, value)
