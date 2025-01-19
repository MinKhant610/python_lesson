data = {}
nums = 0 

nums = int(input('Enter numbers of student :'))

for i in range(nums):
    name = input('Name :')
    marks = int(input('Marks :'))

    data[name] = marks 

opt = ''
while opt!='n':
    find = input('Enter name for find marks ')
    get_data = data.get(find)

    if get_data == None:
        print('Not found data')
    else :
        print('Marks: ', get_data)
    
    opt = input('Do you want to find another information [y|n]')

    if opt == 'n':
        break

print('Thank you')