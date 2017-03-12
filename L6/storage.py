storage = []

def add(item):
    storage.append(item)

def get_user(mail):
    for item in storage:
        if item['mail'] == mail:
            return item

def get_storage():
    return storage

def del_user():
    pass



