class Singletone():
    def __new__(cls, *args):
        if not hasattr(cls, 'instanse'):
            cls.instanse = super(Singletone, cls).__new__(cls)
        return cls.instanse

s = Singletone()
print("Created", s, id(s))

s1 = Singletone()
print("Created", s, id(s1))

печать = print
принт = print
печать("Привет мир!")

def repair(func): #тут постоянный аргумент
    def wrapper(x,y):
        return func(x,y) - 1
    return wrapper

@ repair
def add(a,b):
    return a+b+1

print(add(1,2))