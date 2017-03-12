
class Editor:

    def view_document(self):
        return 'You can view document'

    def edit_document(self):
        pass

class ProEditor(Editor):

    def edit_document(self):
        if '123' == input('Pls, enter code: '):
             return 'You can edit document.'
        else:
            return 'You can not edit document. Your editor is OpenSource. Only - view '

while True:

    e = ProEditor()
    print(e.view_document())
    print(e.edit_document())

    if (input('stop - 0; continue - anykey')) == '0':
        break
