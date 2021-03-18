
# lesson7 task1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, str_list):
        self.str_list = str_list

    def __add__(self, other):
        new_matr=Matrix(self.str_list)
        for i in range(len(self.str_list)):
            for j in range(len(self.str_list[0])):
                new_matr.str_list[i][j] = self.str_list[i][j] + other.str_list[i][j]
        return  new_matr
    def __str__(self):
        res=""
        for each in self.str_list:
            res = res+ str(each) + "\n"
        return res
matrA = Matrix([[2,3], [4,4], [7,0]])
matrB = Matrix([[9,3], [1,4], [0,0]])
print(matrA)
print(matrA + matrB)

# # lesson7 task2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes(ABC):
    def __init__(self, name, size, growth):
        self.name = name
        self.size = size
        self.growth = growth

    @abstractmethod
    def expence_fabric(self):
        pass
    @classmethod
    def total_expence_fabric(cls):
        return  sum(cls.total_expence_fabric)

class Suit(Clothes):
    @property
    def expence_fabric (self):
        return self.size / 6.5 + 0.5

class Coat(Clothes):
    @property
    def expence_fabric(self):
        return self.growth * 2 + 0.3


