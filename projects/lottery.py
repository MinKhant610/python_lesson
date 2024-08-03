from random import randint

ran_num1 = randint(0, 9)
ran_num2 = randint(0, 9)

lottery_num = str(ran_num1)+str(ran_num2) # change type for checking 

lottery_list = [] 

total_lot = int(input('Enter total number of lottery :'))

#check total lottery list
while total_lot != 0:
    money = int(input('Enter the money want to bet :'))
    usr_num = str(input('Enter the lottery num :'))
    check_r = str(input('R ? :'))

    lottery_list.append(usr_num)
    # check reverse or not 
    if check_r.upper() == 'R' :
        reverse_num = usr_num[::-1]
        lottery_list.append(reverse_num)
    else :
        reverse_num = 0

    total_lot -= 1

#show random lottery and check win or lose 
print('\nYour lottery num are : ', ' '.join(lottery_list))
print("\n---------------------------------------")
print(f"Today lottery number is {ran_num1}{ran_num2}") 
print("---------------------------------------\n")

lose = True 

for i in lottery_list:
    if (lottery_num == i):
        lose = False
        print('You win the lottery :-) ')
        print('Your money is ', money*80)
    else :
        if lose == False:
            lose = False
        else :
            lose = True
if lose:
    print('You lost your money ~_~ \n')

