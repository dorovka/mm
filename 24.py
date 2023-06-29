import time
def fun_1(fun):
    def fun_2(name):
        print('start')
        x = time.time()
        fun(name)
        x1 = time.time()
        print('end', x1-x)
    return fun_2


@fun_1 #say = fun_1(say)
def say(name):
    z = [x for x in range(1, 1_000_000)]
    print('inside')


say('aAA')


def sum(a,b):
    return a+b
print(sum(1,2))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


Artem = Person('Artem', 23)
print(Artem.name)