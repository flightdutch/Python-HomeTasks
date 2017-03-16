
class Book:

    def __init__(self,new_name,new_year,new_author):
        self.name = new_name
        self.year = str(new_year)
        self.author = new_author
        self.review = []

    def __str__(self):
        return 'Book: ' + self.name + ', ' + self.year + ' ' + self.author

    def __eq__(self, other_book):
        pass

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
print(book1)
book1.show_reviews()
book1.add_review('Cool!!!')
book1.show_reviews()
book1.add_review('Not bad')
book1.show_reviews()
