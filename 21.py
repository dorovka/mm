def gener():
    for x in range(10**6):
        yield x
#for i in gener():
    #print(i**2)


gener2 = (x for x in range(10**6))
#for i in gener2:
    #print(i**2)




my_list1 =[x for x in range(1,10**6)] #занимает в разы больше места во время вычислений, это список
my_list2 =(x for x in range(1,10**6)) #минусы не знаю, иди нахуй, это генератор называется кста, а сверху - нет.
#Генераторы выполняют задачи сразу, одна за другой без остановок, а списки немного ждут и выполненяют все действия за раз



my_list = (x for x in range(3))
mL = [1, 2, 3, 4, 5]
iter_list = iter(mL)

try:
    for i in range(100):
        print(next(iter_list))
except StopIteration:
    print('END')
'''print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
iter_list = iter(mL)
print(next(iter_list))
'''