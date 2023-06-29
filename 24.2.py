class Item:
    def __init__(self, name, price, width):
        self.name = name
        self.price = price
        self.width = width


    def __add__(self, val_1):
        if isinstance(val_1, Item):
            return self.price + val_1.price
        #if type(val_1) == int:
        elif isinstance(val_1, float):
            return self.price + val_1

    def __radd__(self, val_1):
        if isinstance(val_1, Item):
            return self.price + val_1.price
        #if type(val_1) == int:
        elif isinstance(val_1, float):
            return self.price + val_1

    def __iadd__(self, val_1):
        #if type(val_1) == int:
        if isinstance(val_1, int):
            self.price += val_1
            return self



    def __sub__(self, val_1):
        if isinstance(val_1, Item):
            return self.price - val_1.price
        #if type(val_1) == int:
        elif isinstance(val_1, float):
            return self.price - val_1

    def __rsub__(self, val_1):
        if isinstance(val_1, Item):
            return val_1.price - self.price
        #if type(val_1) == int:
        elif isinstance(val_1, float):
            return val_1 - self.price

    def __isub__(self, val_1):
        #if type(val_1) == int:
        if isinstance(val_1, int):
            self.price -= val_1
            return self



    def __mul__(self, val_1):
        if isinstance(val_1, Item):
            return self.price * val_1.price
        # if type(val_1) == int:
        elif isinstance(val_1, float):
            return self.price * val_1

    def __rmul__(self, val_1):
        if isinstance(val_1, Item):
            return val_1.price * self.price
        # if type(val_1) == int:
        elif isinstance(val_1, float):
            return val_1 * self.price

    def __imul__(self, val_1):
        # if type(val_1) == int:
        if isinstance(val_1, int):
            self.price *= val_1
            return self



    def __truediv__(self, val_1):
        if isinstance(val_1, Item):
            return self.price / val_1.price
        # if type(val_1) == int:
        elif isinstance(val_1, float):
            return self.price / val_1

    def __rtruediv__(self, val_1):
        if isinstance(val_1, Item):
            return val_1.price / self.price
        # if type(val_1) == int:
        elif isinstance(val_1, float):
            return val_1 / self.price

    def __itruediv__(self, val_1):
        # if type(val_1) == int:
        if isinstance(val_1, int):
            self.price /= val_1
            return self



item = Item('Monitor', 123, 10)
print(item.name)
item2 = Item('Mouse', 60, 2)
result = item + item2
print(result)
result1 = item + 1.0
print(result1)
result2 = 2.67 + item
print(result2)
result3 = item - 32.0
print(result3)
result4 = 200.0 - item
print(result4)
result5= item2-item
print(result5)
result6 = item * 32.0
print(result6)
result7 = 200.0 * item
print(result7)
result8= item2*item
print(result8)
result9 = item / 32.0
print(result9)
result10 = 200.0 / item
print(result10)
result11= item2/item
print(result11)
item+=10
print(item.__dict__)