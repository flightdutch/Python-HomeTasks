#!python3.5
# 1) Нужно узнать было ли (ушло/пришло) письмо с определенного почтового адреса (внутреннего/внешнего)?
# 2) Список почтовой активности:
#  - кто, сколько, куда, кому
#  - от кого сколько куда кому
# 3) Список почтовых адресов
# 3) Общий объем избыточности почты (дедупликация)
# 4) Получить точный размер почтовых сообщений, прошедших через SMTP-сервер.
# 5) максимальное/минимальное почтовое сообщение
# Поиск письма в папке SPAM
# Восстановить из папки SPAM
# Добавить адрес в white-list

import class_postfix_log
#from collections import Counter
import collections
import csv

# раскраски
WHITE = '\033[1;m'
GREEN = '\033[1;32m'
LIGHT_CYAN = '\033[1;36m'
RED = '\033[1;31m'
pl = class_postfix_log.MyPostfixLog()

# Check state of mail
def m_way():
    pass

# Фильтр inside FROM-TO
def m_user():
    #email = input('Введите адрес пользователя: ')
    email = 'mandaditos1029@gmail.com'
    m_user = pl.get_mails_from(email)
    d_m_user = collections.Counter(m_user)
    print('My user {} received mails from: '.format(email))
    n = 0
    for key in d_m_user:
        n += 1
        print('N {}. EMAIL-addr: {}  N mails: {}'.format(n, key, d_m_user[key]))
    print('---------------------------------------------')
    print(' Total received mails: ', len(m_user))
    print()

    write_csv('mails_to_'+email+'.csv', d_m_user)

# Print all e-mail addresses passed through the host
def m_list():
    print('...processing file. wait...')
    mails = pl.get_list_emails()
    d_mails = collections.Counter(mails)
    for key in d_mails:
        print('EMAIL-addr: {}  N mails: {}'.format(key, d_mails[key]))

    # import dict to csv-file
    write_csv('mail_list.csv', d_mails)


# Print all IP-addresses connected with the host
def ip_list():
    print('...processing file. wait...')
    ips = pl.get_list_ips()
    d_ips = collections.Counter(ips)
    for key in d_ips:
        print('IP-addr: {}  N attempts connection: {}'.format(key, d_ips[key]))

    # import dict to csv-file
    write_csv('ip_list.csv', d_ips)

def write_csv(f_name, dict):
    with open(f_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Address', 'Frequency']
        writer.writerow(header)
        for key in dict:
            writer.writerow( (key, dict[key]) ) # writerow uses only 1-parameter

        csvfile.close()
        print()
#
# def dict_1dimentional_sort(mydict):
#     mydict = collections.OrderedDict(sorted(mydict.items()))
#     for key, value  in mydict.items(): print(key, value)
#     return mydict

# Create dictionary
operations = {
    '1': m_way,
    '2': m_user,
    '3': m_list,
    '4': ip_list,
}


def main():

    while True:
        print("""
 1. Анализ прохождения письма (do not make)
 2. Найти все письма From-TO (inside user)
 3. Список почтовых адресов прошедших через узел
 4. Список IP-адресов контактировавших c узлом
 5. Выход
    """)
        op = input(LIGHT_CYAN +'-> '+ WHITE)
        try:
            if op in operations.keys():  # проверка наличия ключа
                print(operations[op]())
            elif op =='5':    # Выход
                break
            else:
                print('Неверно. Повторите ввод.')
        except KeyError:
            print('i do not understand you. repeat')


if __name__ == '__main__':
    main()