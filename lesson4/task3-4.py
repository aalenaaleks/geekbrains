
# lesson4 task 3
new_list = [el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0 ]
print(new_list)



# lesson4 task 4
def ver(arg_l, arg_el):
    meetAlready=False
    for el in arg_l:
        if el == arg_el:
            if meetAlready==False:
                meetAlready=True
            else:
                return False
    return True
your_list = (input("Введите список "))
your_list = your_list.split()
#print(your_list)
#print(ver(your_list,'1'))
#print(ver(your_list,'3'))
new_list2 = [el for el in your_list if ver(your_list, el)]
print(new_list2)