#Наследствие мы рассматривали раньше


#Полиморфизм
a = [1,2,3]
b = '123'

print(len(a),len(b))
print(type(a), type(b))


#Инкапсуляция
class A():
    def public(self):
        return 75
    def _protect(self):
        return True
    def _private(self):
        return 'test'
    def wrapped(self):
        return self._private()
    def wrapped_protect(self):
        return self._protect()
a = A()
b = A()
print(id(a), id(b))

print(a.public())
print(a.wrapped())
print(a._private())
print(a.wrapped_protect())

print(a._A_protect())