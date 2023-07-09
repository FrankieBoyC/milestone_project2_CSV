"""
Concerned with retrieving and storing books from a CSV file.
Format of the CSV file is as follows:
name,author,read
"""

books_file = "books.txt"


def create_book_table():
    """Makes sure the CSV file exists."""
    with open(books_file, 'w'):
        pass


def get_all_books():
    """Gets all books from the CSV file."""
    try:
        with open(books_file, 'r') as file_reader:
            lines = [line.strip().split(',') for line in file_reader.readlines()]

            return [
                {'name': line[0], 'author': line[1], 'read': (line[2])}
                for line in lines
            ]
    except IOError:
        print("Error: File not found!")


def _save_all_books(books):
    """Rewrites the CSV file."""
    try:
        with open(books_file, 'w') as file:
            for book in books:
                file.write(f"{book['name']},{book['author']},{book['read']}\n")
    except IOError:
        print("Error: File not found!")


def add_book(name, author):
    """Adds a book to the CSV file."""
    try:
        with open(books_file, 'a') as file:
            file.write(f'{name},{author},0\n')
    except IOError:
        print("Error: File not found!")


def read_book(name):
    """Iterates through the file and marks the users book as read."""
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(name):
    """Removes a book from the CSV file."""
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)





