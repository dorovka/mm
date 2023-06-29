class Employee:
    def __init__(self, name, is_good_employee, on_vacation, salary):
        self.name = name
        self.is_good_employee = is_good_employee
        self.on_vacation = on_vacation
        self.salary = salary
    def info(self):
        return f'name: {self.name}, on vacation? -{self.on_vacation}, salary: {self.salary}, is good? -{self.is_good_employee}'

Artem = Employee('Artem', True, True, 50000)
Valera = Employee('Valera', True, False, 42000)
Nikolai = Employee('Nikolai', False, False, 38000)
Ivan = Employee('Ivan', True, False, 47500)
Nadia = Employee('Nadia', True, True, 36700)
Sotrudniki = [Artem, Valera, Nikolai, Ivan, Nadia]

for x in Sotrudniki:
    if not x.is_good_employee:
        print(f'{x.name} уволен')