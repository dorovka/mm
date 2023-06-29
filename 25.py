from typing import Iterator
from pprint import pprint
goods = [
    {
    'name' : 'Phone',
    'price' : 400,
    },

    {
    'name' : 'poopy',
    'price' : 5,
    },

    {
    'name' : 'PC',
    'price' : 2000,
    },

    {
    'name' : 'PC',
    'price' : 1600,
    },
]


'''def sort(item):
    return item['price']
r = sorted(goods,key = sort)'''
r = sorted(goods, key = lambda item: item['price'], reverse=True)
print(r)
pprint(goods)
PC_list = filter(lambda item: item['name'] == 'PC', goods)
pprint(isinstance(PC_list, Iterator))
#next(PC_list)
print(list(PC_list))




veg = {'carrot': 'veget',
       'color' : 'orange',
       'form' : 'cool'}
x = sorted(veg, key=len)
print(x)
print(veg.keys())
print(veg.items())
print(veg.values())
print(veg['carrot'])





number_list = ['1', '2', '3', '4', '5']
print(type(number_list[1]))
number_list = map(int, number_list)
x = list(number_list)
print(type(x[1]))

num = [1, 2, 3, 4, 5, 6]
num_1 = map(lambda a: a+1, num)
print(list(num_1))


square = lambda a: a*a
summ = lambda a,b: a+b
print(summ(10,10))

def sq(a):
    return a*a
print(sq(4))
print(square(4))



names_l = ['Женя', 'Иван', 'Даниил']
surnames_l = ['Яковлева', 'Серафимович', 'Кожевников']

ns_l = map(lambda x,y:f'{x} = {y}', names_l, surnames_l)
print(list(ns_l))
