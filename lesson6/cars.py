"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model

        #получение текущего года
        curent_year = 2024
        if year > curent_year:
            raise ("Машина еще не выпущена")
        else:
            self.year = year


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
