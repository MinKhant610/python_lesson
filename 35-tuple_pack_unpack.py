#pack 
a = 10
b = 20
c = 30
d = 40 

tuple_ = a, b, c, d 
print(tuple_)
print(type(tuple_))

#unpack 
tuple_1 = (10, 20, 30, 40, 50)
a, b, c, d, e = tuple_1 
print(a, b, c, d, e)

# comprehension 
# comprehension in list 

list_ = [i for i in range(6)]
print(list_)

# comprehension in tuple 
tuple_ = (i for i in range(6))
print(tuple_)

for i in tuple_:
    print(i)