# variable length arguments

def nums(*num):
    print(num)

nums('Min Khant', 20, 'Mechatronics')

def sums(*nums):
    result = 0 
    for num in nums:
        result += num 
    # print(sum(nums))
    return result 

print(sums(1, 2, 3, 4, 5))