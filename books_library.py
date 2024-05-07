import json
from book import Book


class Book_library:
    def __init__(self):
        self.books = []
        self.load_library()

    def get_book(self):
        return self.books

    def add_book(self, book):
        book1 = self.is_book_in_list(book.get_name())
        if book1 is None:
            self.books.append(book)
            print("book has benn added successfully")
            self.save_library()
        else:
            print("the book is on the list")

    def is_book_in_list(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return None

    def add_note(self, name_of_the_book, note):
        book = self.is_book_in_list(name_of_the_book)
        if book is not None:
            book.add_personal_note(note)
            print("note had been added successfully ")
        print("book name are not in the list")

    def mark_book_as_read(self, name_of_the_book):
        book = self.is_book_in_list(name_of_the_book)
        if book is not None:
            book.mark_book_as_read()
            print("book has been marked as read successfully ")
        print("book name are not in the list")

    def mark_book_as_unread(self, name_of_the_book):
        book = self.is_book_in_list(name_of_the_book)
        if book is not None:
            book.mark_book_as_unread()
            print("book has been marked as unread successfully", end="")
        print("book name are not in the list")

    def filter_books_by_author(self, author):
        filtered_books = [book for book in self.books if book.author == author]
        return filtered_books

    def display_list(self, filtered, author):
        if filtered:
            books = self.filter_books_by_author(author)
        else:
            books = self.books
        conunt = 1
        for book in books:
            print(f"{conunt}) {book.display_book_info()}")
            conunt += 1

    def remove_book(self, name):
        book = self.is_book_in_list(name)
        if book is not None:
            self.books.remove(book)
            print(f"{book.get_name()} has been removed from the list")
        else:
            print("book not in the list")

    def save_library(self):
        with open('library.json', 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def load_library(self):
        try:
            with open('library.json', 'r') as f:
                data = json.load(f)
                self.books = [Book(book['name'], book['year'], book['author'], book['gener'], book['is_read'], book['personal_note']) for book
                              in data]
        except FileNotFoundError:
            print("Library file not found. Starting with an empty library.")
