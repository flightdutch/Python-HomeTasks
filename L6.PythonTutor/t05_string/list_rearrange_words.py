# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и инструкцией if.

while True:
    l_words = input('Ввести 2-а слова разделенных пробелом: ')

    l = l_words.index(' ')
    print(l_words[l+1:] + ' ' + l_words[:l+1])

    if input('anykey - continue; 0 - stop:') == '0':
        break