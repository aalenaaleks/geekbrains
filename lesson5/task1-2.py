#lesson5 task1
#Создать программно файл в текстовом формате,
#записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка

my_file = open("my_file1.txt", 'w')
while True:
    data = input("Введите данные " )
    if data == "":
        break
    my_file.write(data + "\n")
my_file.close()


#lesson5 task2
#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open("my_file2.txt", 'r')
counter = 0
while True:
    content = my_file.readline()
    content = content.split()
    print(len(content))
    if content == []:
        break
    counter = counter + 1
print("Количество строк: ", counter)
my_file.close()






