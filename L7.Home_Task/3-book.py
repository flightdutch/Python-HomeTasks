class A:
    pass

class Book:

    def __init__(self,new_name,new_year,new_author):
        self.name = new_name
        self.year = str(new_year)
        self.author = new_author
        self.review = []

    def __str__(self):
        return 'Book: ' + self.name + ', ' + self.year + ' ' + self.author

# http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.author == other.author and self.year == other.year
        return NotImplemented

    def add_review(self, new_review):
        self.review.append(new_review)

    def show_reviews(self):
        n = 1
        for item in self.review:
            print(str(n) + ': ' + item)
            n += 1


book1 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book3 = Book('Над пропастью во ржи', 1951, 'Jerome David Salinger')
book4 = A()
print(book1)
book1.show_reviews()
book1.add_review('Cool!!!')
book1.show_reviews()
book1.add_review('Not bad')
book1.show_reviews()
print('Check __eq__ function')
print(book1 == book2)
print(book1 == book3)
print(book1 == book4)