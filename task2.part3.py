words = input("Введите любые слова через пробелы: ").split() # в список
sort_func = sorted(words, key=len) #сортирует

con_to_str = " ".join(sort_func) #убирает кавычки

print(con_to_str)