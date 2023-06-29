class CHEBUPEK:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('я родился')

    def inf(self):
        print(f'{self.name} {self.age}')

human1 = CHEBUPEK('Pavlusha', 11)
human1.inf()
CHEBUPEK.inf(human1)

human1 = CHEBUPEK('Шелби', 13)
human1.inf()