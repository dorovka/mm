print(int("244", 6))


a = 77
n = ""
SS = 13
k = 0
k2 = 0
while a > 0:
     n = n + str(a % SS)
     a = a // SS
n = list(reversed(n))
print(n)
#print(k)
