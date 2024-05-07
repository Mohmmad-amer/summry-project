from books_library import Book_library, Book


GENR_LIST = ['None', 'Fiction', 'Dystopian', 'Classic', 'Romance', 'Fantasy', 'Science Fiction', 'Adventure',
                 'Historical']

def main():
    library = Book_library()

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. add note to book Book")
        print("4. Delete Book")
        print("5. mark book as read")
        print("6. mark book as unread")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                name = input("Enter book title: ")
                year = int(input("Enter publication year: "))
                author = input("Enter author: ")
                counter = 0
                for genre in GENR_LIST:
                    print(f"{counter}) {genre}")
                    counter += 1
                option = int(input("choose genre from option above: "))
                genre = GENR_LIST[option]
                book = Book(name, year, author, genre, False, "")
                library.add_book(book)
            except Exception:
                print(f"error has been found{Exception}")


        elif choice == '2':
            choice_two = input("if you want to filter by author insert author name or press enter: ")
            if choice_two == "":
                library.display_list(False, choice_two)
            else:
                library.display_list(True, choice_two)

        elif choice == '3':
            name = input("Enter the title of the book to edit: ")
            note = input(f"write the note you want to add to {name} ")
            library.add_note(name, note)

        elif choice == '4':
            name = input("Enter the title of the book to delete: ")
            library.remove_book(name)

        elif choice == '5':
            name = input("Enter the title of the book to mark as read: ")
            library.mark_book_as_read(name)

        elif choice == '6':
            name = input("Enter the title of the book to mark as unread: ")
            library.mark_book_as_unread(name)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
