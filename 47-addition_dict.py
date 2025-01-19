string = input('Enter String: ')
data = {} 

for i in string:
    data[i] = data.get(i, 0) +1

print(data)

for key, value in data.items():
    print(key, '==>', value, 'times')
