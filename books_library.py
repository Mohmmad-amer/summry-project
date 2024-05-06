import json

from book import Book


class Book_library:
    def __init__(self):
        # books = [
        #     Book("To Kill a Mockingbird", 1960, "Harper Lee", "Fiction", False),
        #     Book("1984", 1949, "George Orwell", "Dystopian", False),
        #     Book("The Great Gatsby", 1925, "F. Scott Fitzgerald", "Classic", False),
        #     Book("Pride and Prejudice", 1813, "Jane Austen", "Romance", False),
        #     Book("The Catcher in the Rye", 1951, "J.D. Salinger", "Coming-of-Age", False),
        #     Book("The Hobbit", 1937, "J.R.R. Tolkien", "Fantasy", False),
        #     Book("Brave New World", 1932, "Aldous Huxley", "Science Fiction", False),
        #     Book("The Lord of the Rings", 1954, "J.R.R. Tolkien", "Fantasy", False),
        #     Book("To the Lighthouse", 1927, "Virginia Woolf", "Modernist", False),
        #     Book("Animal Farm", 1945, "George Orwell", "Satire", False),
        #     Book("Crime and Punishment", 1866, "Fyodor Dostoevsky", "Psychological Fiction", False),
        #     Book("The Picture of Dorian Gray", 1890, "Oscar Wilde", "Gothic", False),
        #     Book("Moby-Dick", 1851, "Herman Melville", "Adventure", False),
        #     Book("One Hundred Years of Solitude", 1967, "Gabriel Garcia Marquez", "Magical Realism", False),
        #     Book("The Stranger", 1942, "Albert Camus", "Existentialism", False),
        #     Book("Frankenstein", 1818, "Mary Shelley", "Gothic", False),
        #     Book("The Grapes of Wrath", 1939, "John Steinbeck", "Social Commentary", False),
        #     Book("Beloved", 1987, "Toni Morrison", "Historical Fiction", False),
        #     Book("The Road", 2006, "Cormac McCarthy", "Post-Apocalyptic", False),
        #     Book("Gone with the Wind", 1936, "Margaret Mitchell", "Historical Fiction", False)
        # ]

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
