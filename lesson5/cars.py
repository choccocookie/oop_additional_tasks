"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:
    def __init__(self, brand, model, version):
        self.brand = brand
        self.model = model
        self.version = version

    def get_set_del(self):
        self.brand = 'Kia'
        del self.model
        self.model = 'Optima'
        self.version = '2012'




class CarSlots:

    __slots__ = ('brand', 'model', 'version')

    def __init__(self, brand, model, version):
        self.brand = brand
        self.model = model
        self.version = version

    def get_set_del(self):
        self.brand = 'Geely'
        del self.model
        self.model = 'Tiggo'
        self.version = '2019'


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print((t1-t2)/t1*100)
