# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов,
# заключенную между первым и последнием появлением буквы h, в противоположном порядке.

while True:
    s = input('Ввести cтроку содержащуюю 2 буквы h: ')

    print((s[:(s.find('h'))]) + s[s.rfind('h') - 1:s.find('h'):-1] + (s[(s.rfind('h')) + 1:]))
    print(s)

    if input('anykey - continue; 0 - stop:') == '0':
        break