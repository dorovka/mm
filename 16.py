#args(список) - поизиционные аргументы, kwargs(словарь) - именованные аргументы.
"""def cc(a, b, c=3):
    print(c)
    return a + b
print(cc(b = 5, a = 11, c = 15))"""

def func(a,b, *args, **kwargs):
    c= kwargs.get('c', 3) #если c не найдёт, выведет 3
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1, 2, "132123", [12, 234, 34], True, one = 1, two = 'два', c = 6)



"""def summ(*args):
    s = 0
    for i in args:
        s+=i
    return s
print(summ(1,23,1,23,421))
"""



age = 17
if age >=18:
    is_allow = True
else:
    is_allow = False
#тернарный оператор

is_allow = True if age >= 18 else False
#is_allow = age >=18





val = [1, 2]
if None:
    res = val
else:
    res = []


res = [] if val == None else val


res = []
res = val or res
print(res)





List = []
for i in range(1, 101):
    if i % 5==0:
        List.append(i)
print(List)

 #[VAR тернарный оператор for VAR in Iter Тернарный оператор]
List = [i for i in range(1,101) if i%5 == 0]
print(List)



div_5 = [i**2 if i<50 else i**3 for i in range(1,101) if i%5 == 0]
print(div_5)

a = {x:len(x) for x in ['orange', 'blue', 'gold', 'Mr. Brown']}
print(a)

#False = 0, None, False


new_list = [i for i in range(1,251) if i %30==0 or not(i%31)] #если i = 31, то i%31 = 0, это False, значит функция выполняться не будет, поэтому нужен not
print(new_list)