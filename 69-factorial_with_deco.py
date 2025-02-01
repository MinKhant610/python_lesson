def memorize(fact):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fact(n)
        return cache[n]
    return inner 

@memorize 
def fact(n):
    print(f'Calculating {n}!')
    return 1 if n < 2 else n*fact(n-1)

print(fact(5))
print(fact(6))
