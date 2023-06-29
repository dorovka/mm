class MyFile:
    def __init__(self, name, func):
        self.name = name
        name = name
        self.func = func
        if func == 'w':
            f = open(name, func)
            data = f.write('-')
            print(data)
            f.close()
        elif func == 'r':
            f = open(name, func)
            print(*f)
            f.close()
        else:
            print('некорректный запрос')
Text = MyFile('text.txt', 'r')
