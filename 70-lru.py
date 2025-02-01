from functools import lru_cache 

# lru maxsize = 128 
@lru_cache(maxsize=None)
def fact(n):
    print(f'Calculating {n}!')
    return 1 if n < 2 else n*fact(n-1)

print(fact(5))
print(fact(6))
