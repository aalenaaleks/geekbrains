
# task 3
num_month = int (input ("Введите номер месяца "))
list_month = [ "зима", "зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print(list_month[num_month])


# task 4
your_string = str(input ("Введите строку "))
your_string = your_string.split( )
# print(list(your_string))
for ind, el in enumerate(list(your_string), 1) :
    if len(el) > 10 :
        el = el[:10]
    print(ind, el)