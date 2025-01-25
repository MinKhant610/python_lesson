def data(name, age):
    print('Name :', name)
    print('Age :', age)

# positional arguments
data('Min Khant', 20)

# keyword arguments
data(age=21, name='MinKhant')

# default arguments
def mydata(name, age=20):
    print('Name :', name)
    print('Age :', age)

mydata('Min Khant')

