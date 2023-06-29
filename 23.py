import time

class Person:
    def __init__(self, name):
        self.name = name


Artem = Person('Artem')
print(Artem.name)

class open:
    def __init__(self, name, mod):
        self.name = name
        self.mod = mod
        self.t = None

    def __enter__(self):
        self.t= open(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t.close()

p = open

class run:

    def __init__(self):
        self.start = None

    def __enter__(self):
        print('мы внутри')
        self.start= time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f't = {t} exc_type = {exc_type} exc_val = {exc_val} exc_tb = {exc_tb}')
        if exc_type is TypeError:
            return True

with run() as t:
    x = [x for x in range(1, 1_000_000)]
    x -= 's'
    print(t)
