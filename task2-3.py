# задание 2

t = input("Введите время в секундах ")
t = int(t)
h = t // 360
m = (t - h * 360) // 60
s = (t - h * 360 - m * 60)

if h > 24:
   h = h % 24

elif h < 10:
    h = "0" + str(h)

if m < 10:
    m = "0" + str(m)

if s < 10:
    s = "0" + str(s)

hhmmss = f"{h} : {m} : {s}"
print(hhmmss)

# задание 3
a = input("Введите число ")
a = int(a)
print(a*100 + a*20+ 3*a)

