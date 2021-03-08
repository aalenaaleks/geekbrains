# Lesson5 task5
#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open("my_file5.txt", 'w')
sum = 0
while True:
    data = input("Введите число " )
    my_file.write(data + " ")
    if data == "":
        break
    sum = sum + int(data)
print('Сумма = ', sum)
my_file.close()
