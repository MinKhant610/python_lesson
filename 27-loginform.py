#login form 
#step 1 -> original name and pass -> done 
#step 2 -> name -> done 
#step 3 -> password -> done 
#step 4 -> check name and password -> done 
#setp 5 -> if ture -> login success -> done 
#step 6 -> if false -> login fail -> done 
#step 7 -> if fase 2 time -> sorry try again and later -> done 

user_name = 'minkhant'
user_pass = 123456 
counter = 0

while counter < 2:
    name = input('Enter your name :')
    password = int(input('Enter your password :'))

    if name == user_name and password == user_pass:
        print('Login success')
        break
    else :
        print('login fail')
        counter+=1
        if (counter == 2):
            print('try again and later ')

