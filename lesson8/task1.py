# lesson 8 task1
#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
#  должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#  Проверить работу полученной структуры на реальных данных.



class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def list (cls,data):
        dates=[]
        lst=data.split("-")
        dates.append(int(lst[0]))
        dates.append(int(lst[1]))
        dates.append(int(lst[2]))
        return dates

    @staticmethod
    def dayCorrect(dates):
        if dates[0] > 31 or dates[0] < 1:
            return False
        if dates[1] > 12 or dates[1] < 1:
            return False
        return True

a = Data.list(input("Введите дату "))
print("Результат валидации данных:", Data.dayCorrect(a))
print("Число ", a[0])




