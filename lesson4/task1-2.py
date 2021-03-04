
# lesson4 task 1
from sys import argv

salary, time, rate, prize = argv

print("Имя скрипта: ", salary)
print("Параметр 1: ", time)
print("Параметр 2: ", rate)
print("Параметр 3: ", prize)
def salary(time, rate, prize):
    return time * rate +prize
print('Your salary is ', salary(int(time),int(rate),int(prize)))


# lesson4 task 2
list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
k = 0
while k < int(len(list)-1):
    if int(list[k + 1]) > int(list [k]):
        new_list.append(int(list[k+1]))
    k = k + 1
print(new_list)



