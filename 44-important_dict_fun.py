data = {1:'Min Khant', 2:'Han Lin Oo', 3:'Zin Zin Win Htet'}

#get data
print(data[1])
print(data.get(1))
# print(data[4])
print(data.get(4))
print(data.get(1, 'Zin Zin'))
print(data.get(4, 'Myat Thu'))

print(data)

#delete data 
print(data.pop(2))
print(data)

#copy 
data2 = data.copy()
print(data2)

