def myfun():
    print('hello')

myfun()

#lambda function 
mylambda = lambda : 'hello'
print(mylambda())

def add(num1, num2):
    print(num1 + num2)

add(2, 4)

addlambda = lambda num1, num2 : num1 + num2
print(addlambda(2, 4))

# Write a program to identify the larger of two numbers using the lambda
# function

def biggest(num1 , num2):
    if num1 > num2 :
        return num1 
    else:
        return num2 

print('Biggest :', biggest(2, 4))

biggestLam = lambda num1, num2 : num1 if num1 > num2 else num2
print('Biggest :', biggestLam(2, 4))