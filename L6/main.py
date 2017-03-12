import storage

def show(elements):
    st = storage.get_storage()
    for item in st:
        print(item)

def run():
    while True:
        data = {}
        data['name'] = input('Name: ')
        data['mail'] = input('Mail: ')
        data['passw'] = input('Password: ')
        storage.add(data)
        show()

        if input('anykey - continue; 0 - stop: ') == '0':
            break


