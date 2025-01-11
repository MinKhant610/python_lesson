tuple1 = (10, 20, 30)
tuple2 = (40, 50 ,60)
tuple1 += tuple2 
print(tuple1)

# Repetition Operator (*)
tuple_ = (100, 200)
tuple_ *= 3
print(tuple_)

print('length of tuple_', len(tuple_))
print('count :', tuple_.count(100))
print('index :', tuple_.index(200))

my_tuple = (400, 100, 300, 200)
print(my_tuple)
sorted_tuple = sorted(my_tuple, reverse=True)
print(sorted_tuple)
print(type(sorted_tuple))

print('Min value in my tuple', min(my_tuple))
print('Max value in my tuple', max(my_tuple))