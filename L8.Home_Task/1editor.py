license_key = '1234567890'

class Editor:

    def view_document(self):
        return 'You can only view document'

    def edit_document(self):
        pass

class ProEditor(Editor):

    def view_document(self):
        return 'You can edit document.'

    def edit_document(self):
        pass

while True:
    if license_key == input('Pls, enter license code: '):
        e = ProEditor()
    else:
       e = Editor()

    print(e.view_document())

    if (input('stop - 0; continue - anykey')) == '0':
        break
