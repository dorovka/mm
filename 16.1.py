#unmuteble -tuple(кортедж[]), bool, int, float, string, bytes, complex, fronzenset
#muteble - все остальные

x ="32"
y = "32"
z = x[1]


print(id(x), id(y), id(z))
print(x is y) #проверяет равны ли по id

l = [1,2,3]
m=l
l.append(5)
m.append(7)
print(l is m)

some_tuple = tuple(l)
print(some_tuple)
some_list = list(some_tuple)
some_list.append(3)
print(some_list)

tuple_1 = ([1,2,3],2, "1234")
tuple_1[0].append(4)
print(tuple_1)