import time

class clasSchet:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.limit +=1
        time.sleep(0.5)
        return  self.limit

iter = clasSchet(0)


while iter!=0:
    print(next(iter))