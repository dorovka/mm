a = int(input())
b = int(input())
oper = input()

def schet(a, b, oper):
    def add(a,b):
        return a+b

    def dif_2(a,b):
        return a-b

    def On(a,b):
        return a * b

    def In(a,b):
        return a / b

    calc = {"+":add,
            "-":dif_2,
            "*":On,
            "/":In}

    print((calc[oper](a,b)))

    global otvet
    otvet = str(calc[oper](a,b))



schet(a, b, oper)

final = open("text.txt", "w")
final.write(otvet)
final.close()