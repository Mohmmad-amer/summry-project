class Book:
    def __init__(self, name, year, author,genre, is_read, personal_note):
        self.name = name
        self.year = year
        self.gener = genre
        self.author = author
        self.is_read = is_read
        self.personal_note = personal_note

    def mark_book_as_read(self):
        self.is_read = True

    def mark_book_as_unread(self):
        self.is_read = False

    def add_personal_note(self, s):
        self.personal_note = s

    def display_book_info(self):
        return (f"name: {self.name}\nyear: {self.year},"
                f" gener: {self.gener} ,auther: {self.author}, "
                f"read status:{self.is_read}. \npersonal note:{self.personal_note}")

    def get_name(self):
        return self.name
