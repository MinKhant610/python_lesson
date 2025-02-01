def method():
    yield 'p'
    yield 'q'
    yield 'r'

gen = method()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
