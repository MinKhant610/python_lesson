string = input('Enter String :')
vowels = {'a', 'e', 'i', 'o', 'u'}
data = {} 

for i in string:
    if i in vowels:
        data[i] = data.get(i, 0) + 1 

for key, value in sorted(data.items()):
    print(key, '==>', value, 'times')