### 1
a,b = input('введите два числа').split()
a,b = map(float,(a,b))
if b == 0:
   print ('del is 0')
else:
   print (a/b)

### 2
a = int(input('summa'))
skidka=0
sum = a
if a > 20:
    a=a - a/100*35
    skidka=sum-a
print('стоимость = ',round(a,2),'скидка  = ',round(skidka,2))

### 3
a = int(input('Введите число от 1 до 12 '))
if a > 12:
    print ('ошибка')
elif a == 1:
    print ('january winter')
elif a == 2:
    print ('february winter')
elif a == 3:
    print ('march spring')
elif a == 4:
    print ('april spring')
elif a == 5:
    print ('may spring')
elif a == 6:
    print ('june summer')
elif a == 7:
    print ('july summer')
elif a == 8:
    print ('august summer')
elif a == 9:
    print ('september autumn')
elif a ==10:
    print ('october autumn')
elif a == 11:
    print ('november autumn')
elif a == 12:
    print ('december winter')
