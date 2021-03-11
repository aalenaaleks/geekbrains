# Lesson6 task2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
class Road:
    def __init__(self, length, width, name=""):
        self._length = length
        self._width = width
        self._name = name

    _massa1kvm = 25
    _fat = 3

    def massa_asf(self):
        massa = self._length * self._width * self._massa1kvm * self._fat
        return massa

a = Road(3,4, "Doroga1")
b = Road(100,3)
print(a._name, ":", a.massa_asf())
print(b._name, ":", b.massa_asf())