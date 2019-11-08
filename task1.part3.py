words = list(input('Введите слово: '))
# Пустой Список
list1 = []       #
list2 = []
for letter in words:# по одному
    if letter.isupper(): # сравнение
        list1.append(letter)
    elif letter.islower(): #сравнение
        list2.append(letter)

sum_of_upper_letters = len(list1)
sum_of_lower_letters = len(list2)     # маленькими
sum_of_all_letters = len(words)    # общее каличесво

percent_of_upper = round((sum_of_upper_letters/sum_of_all_letters)*100, 2)  #проценты выводит
percent_of_lower = round((sum_of_lower_letters/sum_of_all_letters)*100, 2)

print(f'Всего {sum_of_all_letters} букв.')
print(f'Из них {percent_of_upper}% в вверхнем регистре.')
print(f'А {percent_of_lower}% написаны в нижнем регистре.')