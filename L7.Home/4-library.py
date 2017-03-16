
class Book:

    def __init__(self,new_name,new_year,new_author):
        self.name = new_name
        self.year = str(new_year)
        self.author = new_author
        self.reviews = []

    def __str__(self):
        return 'Book: ' + self.name + ', ' + self.year + ' ' + self.author

    def __eq__(self, other_book):
        pass

    def add_review(self, new_review):
        self.reviews.append(new_review)

    def show_reviews(self):
        n = 1
        print('All reviews for "' + self.name + '" is/are:  ' + str(len(self.reviews)))
        for item in self.reviews:
            print(str(n) + ': ' + item)
            n += 1


class Library(Book):

    def __init__(self):
        self.library = []

    def add_book(self, new_book):
        self.library.append(new_book)

    def show_library(self):
        for item in self.library:
            print(item)

book1 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book3 = Book('Над пропастью во ржи', 1951, 'Jerome David Salinger')
print(book1)
print()
mylib = Library()
mylib.add_book(book1)
mylib.add_book(book1)
mylib.add_book(book1)
mylib.show_library()
print()
book1.show_reviews()
book1.add_review('Cool!!!')
book1.add_review('Not bad')
book1.show_reviews()
