# задание 4
user_number = (int(input( "Введите число ")))
max_number = 0
number = user_number % 10

while user_number > 0 :
    if number > max_number :
        max_number = number
    user_number = user_number // 10
    number = user_number % 10
print(max_number)


# задание 5
user_gain = (int(input( "Введите значение выручки  ")))
user_expenses = (int(input( "Введите значение издержек  ")))
if user_gain - user_expenses > 0 :
    print ( str("Ваша прибыль:"), int(user_gain - user_expenses))
    print ( str("Рентабельность выручки:"), float(user_gain - user_expenses) / int(user_gain))
else :
    print ( str("Ваш убыток:"), abs(int(user_gain - user_expenses)))
user_quantity = (int(input( "Введите количество сотрудников  ")))
print ( str("Прибыль в расчете на одного сотрудника :"), (int(user_gain - user_expenses)) / int(user_quantity))


