# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#         print(sum)
# #    print(n)
#
# add(1, 2, 5, 6, 5)

# def calculate(n, n2, **kwargs):
#     print(kwargs)
#     print(kwargs['f'])
#     print(kwargs.get('f2'))
#
# calculate(2, 3, f='add', f='muiltiply')

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = 'Stinger'
        #self.model = kwargs["model"]
        self.model = kwargs.get("model")

my_car = Car(make="kia")
print(my_car.make)
print(my_car.model)