#lesson3 task3
def my_func(arg1, arg2, arg3):
    if arg1 < arg2 and arg1 < arg3:
        return arg2 + arg3
    elif arg2 < arg1 and arg2 < arg3:
        return arg1 + arg3
    return arg2 + arg1
print(my_func(35, -5.7, -44))


#lesson3 task4
# первый способ
def my_func():
    x = int(input("введите действительное положительное число "))
    y = int(input("введите целое отрицательное число "))
    res = x ** y
    return res
res = my_func()
print(res)
#lesson3 task4
# второй способ
def my_func():
    x = int(input("введите действительное положительное число "))
    y = int(input("введите целое отрицательное число "))
    z = list(range(1, abs(y)+1))
    res = 1
    for el in z:
        res = res * x
    return 1 / res
res = my_func()
print(res)

