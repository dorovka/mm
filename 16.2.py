"""chetkooo = []
ne_chetko = []"""""""""

"""for i in range(10):
    n = int(input())
    if n%2 ==0:
        chetkooo.append(n)
    else:
        ne_chetko.append(n)"""




chetkooo = [i for i in range(10)if i%2==0]
ne_chetko = [i for i in range(10) if i%2!=0]
print(chetkooo)


a = (5, 3, 2, 1, 4)
print(tuple(sorted(a)))
