#lesson3 task1
def div(arg1, arg2):
    if arg2 != 0:
        return arg1/arg2
    return "Недопустимое значение аргумента!"
arg1 = int(input("Введите первый аргумент "))
arg2 = int(input("Введите второй аргумент "))
print(div(arg1,arg2))

#lesson3 task2
def user_data(name, surname, year, city, email, telefone):
    return f"{name}, \n{surname}, \n{year}, \n{city}, \n{email}, \n{telefone}"
print(user_data("A", "A", "1979", "A", "email", "ip"))








