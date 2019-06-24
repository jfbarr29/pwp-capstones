class User():
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def __repr__(self):
        return "User: {name}, Email: {email}, Books read: {books}".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name or self.email == other_user.email:
            return "User already exists!"

    def get_email(self):
        return self.email

    def change_email(self):
        new_email = input("What is your new email address? ")
        self.email = new_email
        return self.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0.0
        #rating = 0.0
        for rating in self.books.values():
            if rating == None:
                rating = 0
                total += rating
                average = (total / len(self.books))
            else:
                total += rating
                average = (total / len(self.books))
            #print(total)
            #print(average)
        return average

    def get_books_read(self):
        return len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []

    def __repr__(self):
        return "{title}".format(title=self.title, ratings=self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        if self.title == other_book.title or self.isbn == other_book.isbn:
            return "Book has alrady been rated"

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        return "isbn has been updated to: {isbn}".format(isbn=self.isbn)

    def add_rating(self, rating):
        #print(rating)
        if rating in range(0,5):
            #print(rating)
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        total = 0.0
        #rating = 0.0
        for rating in self.ratings:
            #print(rating)
            if rating == None:
                rating = 0
                total += rating
                average = (total / len(self.ratings))
            else:
                total += rating
                average = (total / len(self.ratings))
            #print(total)
            #print(average)
        return average



class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author, ratings=self.ratings)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject, ratings=self.ratings)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Tome Rater is a collection of users, {users}, and the books they have rated, {books}.".format(users = self.users, books = self.books)

    def __eq__(self, other_tomerater):
        if self.users == other_tomerater or self.books == other_tomerater:
            return "Either a user who has made a rating, or a book that has been rated, exists in this collection, {self}".format(self=self)

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            #print(email)
            #print(rating)
            #print(self.users.get('email'))
            self.users.get(email).read_book(book, rating)
            #print(rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print('No user with email {email}'.format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        #print(new_user)
        self.users[email] = new_user
        if user_books:
            #print(True)
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(self.users.get(user))

    def most_read_book(self):
        highest_book = ' '
        highest_count = 0
        for key, value in self.books.items():
            if value > highest_count:
                highest_book = key
                highest_count = value
        return highest_book

    def highest_rated_book(self):
        high_book = ' '
        high_rate = 0
        for book in self.books:
            if book.get_average_rating() > high_rate:
                high_book = book
                high_rate = book.get_average_rating()
        return high_book

    def most_positive_user(self):
        high_user = ' '
        high_rate = 0
        for user in self.users:
            #print("Hey >")
            #print(user)
            #print(value)
            if self.users.get(user).get_average_rating() > high_rate:
                high_user = self.users.get(user)
                high_rate = self.users.get(user).get_average_rating()
                #print(self.users.get(user))
                #print(high_rate)
        return high_user

    def get_n_most_read_books(self, n):
        newlist = []
        for key, value in self.books.items():
            temp = key, value
            newlist.append(temp)
            sorted_list = sorted(newlist, key=lambda tup: tup[1], reverse=True)
            desc_list = sorted_list[0:n]
        return desc_list

    def get_n_most_prolific_readers(self, n):
        newlist = []
        for user in self.users:
            temp = (user, self.users.get(user).get_books_read())
            newlist.append(temp)
            sorted_list = sorted(newlist, key=lambda tup: tup[1], reverse=True)
            desc_list = sorted_list[0:n]
        return desc_list
        #sorted_list = sorted(newlist, key=lambda tup: tup[1], reverse=True)
        #desc_list = sorted_list[0:n]
        #print(desc_list)
