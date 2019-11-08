num = input('Введите список чисел: ').split(' ') #список
i = [int(i) for i in num]  #числа
l = 1 #флаг

if max(i) < 0:
    l += 0
    print(l)
else:
    while True:
        if l in i:
            l += 1
        elif l not in i:
            print(l)
            break


