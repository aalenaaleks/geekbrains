#lesson5 task3
#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. \
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

f_obj = open("my_file.txt")
sum_cont = 0
counter = 0
while True:
    content = f_obj.readline()
    content = content.split()
    if content == []:
        break
    counter = counter + 1
    sum_cont = sum_cont + int(content[1])
    if int(content[1]) < 20000:
        print(content)
print('average',sum_cont/counter)

f_obj.close()

#lesson5 task4
# Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

russian_orders = ["ноль","Один","Два","Три","Четыре"]
f_obj = open("my_file4.txt", "r")
res_f = open("my_file4_res.txt", "w")
while True:
    content = f_obj.readline()
    content = content.split()
    if content == []:
        break
    #print(russian_orders[int(content[2])])
    new_str = russian_orders[int(content[2])] + " "  + content[1] + " "  + content[2]
    print(new_str)
    res_f.writelines(new_str + "\n")
res_f.close()
f_obj.close()