from pprint import pprint
index_goods = []
goods2 = ['A0', 'A1', 'A2', 'A3']
for i, item in enumerate(goods2):
    index_goods.append({i:item})
    #a = i, item
    #index_goods.append(a)

pprint(index_goods)


surnames_l = ['Яковлева', 'Серафимович', 'Кожевников']
f = 'asdsadsa'
patrion_l = ['Федосьевна', 'Руштенович', 'Олегович']
names_l = ['Женя', 'Иван', 'Даниил']
for name, surname, patrion, g in zip(names_l, surnames_l, patrion_l, f):
    a = g + ' PPtq+', surname, name, patrion
    print(a)