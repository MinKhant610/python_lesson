def myfun(num, *nums):
    print(num, nums)
    for i in nums:
        print(i)

myfun(1, 2, 3, 4)

def myfun2(*nums, num):
    print(nums)
    print('num ', num)

myfun2(1, 2, 3, num=4)

