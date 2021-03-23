#  Lesson8 task2
#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#  Проверьте его работу на данных, вводимых пользователем.
#  При вводе пользователем нуля в качестве делителя
#  программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_ex(Exception):
    def __init__(self, txt):
        self.txt = txt


numerator = int(input("Enter numerator"))
denumerator = int(input("Enter denumerator"))

try:
    if (denumerator==0):
        raise My_ex("Denumerator is zero")
except (ValueError, My_ex) as err:
    print(err)
else:
    print(numerator, "/", denumerator, "=", numerator/denumerator)
