#task1
my_list = [19, 'word', 3856, 7.8, None]
print (len(my_list))
for el in my_list:
  print(type(el))


#task2
your_list = input("Введите список ")
your_list =your_list.split()
n = len(your_list)
print (len(your_list))
print (your_list)
k = 0
list_reverse=[]
while k + 1 < n :
    list_reverse.append(your_list[k+1])
    list_reverse.append(your_list[k])
    k = k + 2
if len(your_list) % 2 != 0:
    list_reverse.append(your_list[n-1])

print (list_reverse)



