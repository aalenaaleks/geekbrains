# lesson6 task4
#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print("Машина поехала.")
    def stop(self):
        print("Машина остановилась.")
    def turn(self, direction):
            print("Машина повернула на ", direction, " градусов")
    def show_speed(self):
        print("Скорость автомобиля ", self.speed)

class TownCar(Car):
    def show_speed(self):
        print("Скорость городского автомобиля ", self.speed)
        if self.speed > 60:
          print("Превышение скорости", self.name)


class WorkCar(Car):
    def show_speed(self):
        print("Скорость рабочего автомобиля ", self.speed)
        if self.speed > 40:
          print("Превышение скорости", self.name)

class SportCar(Car):
    def sport_car(self):
        print("Это класс спортивных автомобилей ")

class PoliceCar(Car):
    def police_car(self):
        print("Это класс полицейских автомобилей ")

a=TownCar(100,"green", "kia", True)
b=TownCar(30,"green", "kia", True)
a.show_speed()
b.show_speed()