# Name      Roll  
# Min Khant 17   

data = {}
nums = 0 

nums = int(input('Enter the number of student :'))

while nums > 0 :
    name = input('Name :')
    roll = int(input('Roll :'))

    data[name] = roll
    nums = nums -1

print('\nName\t\t Roll\t')

for key,value in data.items():
    print(key, '\t', value)
