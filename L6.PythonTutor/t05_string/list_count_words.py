# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.
# Используйте для решения задачи метод count.

while True:
    l_words = input('Ввести слова разделенные 1-м пробелом: ')

    i_counts = l_words.count(' ') + 1
    print(i_counts)

    if input('anykey - continue; 0 - stop:') == '0':
        break
