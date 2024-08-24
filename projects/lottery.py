from random import randint

ran_num1 = randint(0, 9)
ran_num2 = randint(0, 9)
money = 0
r_money = 0
win_money = 0
lose = True 
r_win = False
lottery_num = str(ran_num1)+str(ran_num2) # change type for checking 

lottery_list = [] 
unit = 0 # user add amount 
user_amount = 0
total_bet = 0

#show bet money and current user amount 
def showBetAndAmount(total_bet, user_amount):
    print('\n-----------------------------------------')
    print (f'Total bet {total_bet} units ')
    print ('Now your balance is :', user_amount)

#for money control 
print(f"Today lottery number is {ran_num1}{ran_num2}") 
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

        if user_amount <= 0 :
            break

        print('\n-----------------------------------------')
        money = int(input('Enter the money want to bet :'))
        usr_num = str(input('Enter the lottery num :'))
        check_r = str(input('R ? :'))

        if money > user_amount :
            print('Not enough money')
            showBetAndAmount(total_bet, user_amount)
            break

        lottery_list.append(usr_num)

        # check reverse or not 
        if check_r.upper() == 'R' :
            r_money = int(input('Enter amount of R money :')) 
            temp = money
            money += r_money

            #add total bet and reduce amount 
            if money > user_amount :
                print('Not enough money')
                showBetAndAmount(total_bet + temp, user_amount - temp)
                break
            
            reverse_num = usr_num[::-1]
            lottery_list.append(reverse_num)

            #check if r_money is win or not 
            for i in lottery_list:
                if (lottery_num == i):
                    lose = False
                    r_win = True
                    win_money = r_money * 80
        else :
            reverse_num = 0

        user_amount -= money # reduce user money 
        total_bet += money
        total_lot -= 1 #number of lottery 

        # show total bet money 
        showBetAndAmount(total_bet, user_amount)

# show random lottery and check win or lose 
print('\nYour lottery num are : ', ' '.join(lottery_list))
print("\n---------------------------------------")
print(f"Today lottery number is {ran_num1}{ran_num2}") 
print("---------------------------------------\n")


for i in lottery_list:
    if (lottery_num == i):
        lose = False
        if r_win :
            temp = money * 80
            win_money = temp - win_money
            user_amount = user_amount + win_money
        else :
            win_money = money * 80
            user_amount = user_amount + win_money
        
        print(f'You win {win_money} :-) ')
        print('Now your money is ', user_amount)
    else :
        if lose == False:
            lose = False
        else :
            lose = True
if lose:
    print('You lost your money ~_~ \n')

