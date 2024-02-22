class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def checkout(self):
        if self.is_checkedout: # Ошибка: неправильное имя переменной
            print("This book is already checked out.")
        else:
            self.is_checkedout = True

    def checkin(self):
        if not self.is_checked_out:
            print("This book is not checked out.")
        else:
            self.is_checked_out = False


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books_checked_out = []

    def checkout_book(self, book):
        if book.is_checked_out:
            print("This book is already checked out.")
        else:
            book.checkout()
            self.books_checked_out.append(book)

    def return_book(self, book):
        if book in self.books_checked_out:
            book.checkin()
            self.books_checked_out.remove(book)
        else:
            print("This book was not checked out by the user.")


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        if book.isbn in self.books:
            print("This book is already in the library.")
        else:
            self.books[book.isbn] = book

    def remove_book(self, book):
        if book.isbn in self.books:
            del self.books[book.isbn]
        else:
            print("This book is not in the library.")

    def register_user(self, user):
        if user.user_id in self.users:
            print("This user is already registered.")
        else:
            self.users[user.user_id] = user

    def unregister_user(self, user):
        if user.user_id in self.users:
            del self.users[user.user_id]
        else:
            print("This user is not registered.")

# Использование классов
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
user1 = User("John Doe", 1)

library.add_book(book1)
library.register_user(user1)

user1.checkout_book(book1) # Пользователь берет книгу
user1.return_book(book1) # Пользователь возвращает книгу
