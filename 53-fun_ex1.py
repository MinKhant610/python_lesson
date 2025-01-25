# Program: Write a user- defined function to check whether the number is even or odd.

def checkNum(num):
    if num%2 == 0:
        print('Is Even')
    else:
        print('Is Odd')

checkNum(5)
checkNum(4)

# Write a user- defined function to identify the factorial of a given range of
# numbers.
# 5! = 5 * 4 * 3 * 2 * 1 = 120 
def factorial(num):
    if num <= 1:
        return 1 
    else:
        return num * factorial(num - 1)

print(factorial(5))

# Program: Write a program that calculates the addition and subtraction of two numbers.
def calculates(num1, num2):
    add = num1 + num2 
    sub = num1 - num2 
    return add, sub 

addition, subtraction = calculates(5 , 4)
print('Addition :', addition)
print('Subtraction :', subtraction)

def cal(num1 , num2):
    add = num1 + num2 
    sub = num1 - num2 
    multi = num1 * num2 
    div = num1 / num2 

    return add, sub, multi, div 

results = cal(5, 4)
for result in results:
    print(result)