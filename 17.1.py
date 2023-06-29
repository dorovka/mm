class A:
    def one(self):
        print('one is A')
    def two(self):
        print('two is A')

class C:
    def one(self):
        print('one is C')

class B(A, C):
    def two(self):
        print('two is B')
    def three(self):
        print('three is B')


class B1(C, A):
    def two(self):
        print('two is B')
    def three(self):
        print('three is B')

a = A()
a.one()
a.two()

print('-'*50)

b = B()
b.one()
b.two()
b.three()

print('-'*50)

b1 = B1()
b1.one()
b1.two()
b1.three()
