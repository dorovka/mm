class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def age(self):
        return self.__days

    @age.setter
    def age(self, agg):
        self.__days = agg

    def get_day(self):
        return self.__days
    def set_day(self, new_day):
        if new_day == 365 or new_day == 366:
            self.__days = new_day
        else:
            raise Exception('errorka')

    days = property(fget=get_day, fset = set_day, fdel = None)
y = Year(365, 'Зима')
print(y.__dict__)
#y.__days
#y.__dict__
y.days = 366
y.get_day()
#y.set_day(366)


print(y.__dict__)

class Person:
    def __init__(self, age,name):
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age_1):
        self.__age = age_1

    @age.deleter
    def age(self):
        del self.__age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_1):
        self.__name = name_1

    @name.deleter
    def name(self):
        del self.__name


Artem = Person(20, 'Artem')
print(Artem.__dict__)
Artem.age = 123
print(Artem.age)
del Artem.name
print(Artem.__dict__)
del Artem.age
print(Artem.__dict__)