storage = []

def add_user():
    s =[]
    s.append('name', input('Enter your name: '))
#    s[mail] =  input('Enter your mail: ')
#    s[password] = input('Enter your password: ')
    return s

def get_user():
    pass

def del_user():
    pass

def show_users(elements):
    for element in elements:
        for key, value in element.items():
            print(key,value,end='|')

def main():
    op = int(input('1. Add, 2. Show : '))
    if op == 1:
        storage.append(add_user())
    elif op ==2:
        show_users(storage)

main()
