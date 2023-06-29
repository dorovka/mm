import random

class clasRandom:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -=1
        return  random.randint(1, 100)

random_iter = clasRandom(4)



for i in range(4):
    print(next(random_iter))



try:
    print(next(random_iter))
    print(next(random_iter))
    print(next(random_iter))
    print(next(random_iter))
    print(next(random_iter))
    print(next(random_iter))

except StopIteration:
    print('Stop')