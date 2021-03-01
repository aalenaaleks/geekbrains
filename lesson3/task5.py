#lesson3 task5
y_string = (input("Введите строку "))
y_string = y_string.split()
#print(y_string)
def sum_string(y_string):
    sum_string = 0
    for el in y_string:
        sum_string = sum_string + int(el)
    return sum_string
print(sum_string(y_string))
add_y_string = input("Введите продолжение строки " )
add_y_string = add_y_string.split()
spec = 0
if all el in add_y_string != spec:
    print(sum_string(add_y_string))

# не успела дописать втрую часть этой программы((

