from random import randint

ran_num1 = randint(0, 9)
ran_num2 = randint(0, 9)

lottery_num = str(ran_num1)+str(ran_num2) # change type for checking 

lottery_list = [] 
unit = 0 # user add amount 
user_amount = 0
total_bet = 0


#for money control 
print('\n------------------------------------------')
print('      -----Welcome to lottery bet-----        ')
print('------------------------------------------')
print('You can add at least 1000 or more')
unit = int(input('Enter the money want to add :'))

if unit < 1000:
    unit = 0
    print('Add at least one thousand')
else :
    user_amount += unit 
    print('Now your balance is :', unit)
    total_lot = int(input('Enter total number of lottery :'))

    #check total lottery list
    while total_lot != 0:
        # if user_amount == 0:
        #     print('Not enough money')
        #     break

        print('\n-----------------------------------------')
        money = int(input('Enter the money want to bet :'))
        usr_num = str(input('Enter the lottery num :'))
        check_r = str(input('R ? :'))

        lottery_list.append(usr_num)

        # check reverse or not 
        if check_r.upper() == 'R' :
            r_money = int(input('Enter amount of R money :')) 
            money += r_money
            reverse_num = usr_num[::-1]
            lottery_list.append(reverse_num)
        else :
            reverse_num = 0

        user_amount -= money # reduce user money 
        total_bet += money
        total_lot -= 1 #number of lottery 

        # show total bet money 
        print('\n-----------------------------------------')
        print (f'Total bet {total_bet} units ')
        print ('Now your balance is :', user_amount)


# show random lottery and check win or lose 
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

