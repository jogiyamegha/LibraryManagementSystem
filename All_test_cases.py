import sqlite3

# Connection creation to the database
conn = sqlite3.connect('Library.db')
cursor = conn.cursor()

# Create a book table that contains book information
query1 = '''CREATE TABLE IF NOT EXISTS Book(
            id INTEGER PRIMARY KEY ,
            isbn TEXT UNIQUE,
            book_title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER,
            is_available INTEGER )'''
cursor.execute(query1)
conn.commit()

# Function to add a new book to the library
def add_book():
    id = int(input("Enter book ID: "))
    isbn = input("Enter ISBN: ")
    book_title = input("Enter book title: ")
    author = input("Enter author: ")
    publication_year = int(input("Enter publication year: "))
    is_available = 1  # Newly added books are available by default

    try:
        cursor.execute('''INSERT INTO Book (id, isbn, book_title, author, publication_year, is_available)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (id, isbn, book_title, author, publication_year, is_available))
        conn.commit()
        print(f"Book '{book_title}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"ERROR: Book with ISBN {isbn} already exists.")
    print("")

# Function to borrow a book
def borrow_book():
    isbn = input("Enter ISBN : ")
    cursor.execute('''SELECT is_available FROM Book 
                      WHERE isbn = ?''', (isbn,))
    book = cursor.fetchone()
    if book:
        if book[0] == 1:
            cursor.execute('''UPDATE Book 
                              SET is_available = 0
                              WHERE isbn = ?''', (isbn, ))
            conn.commit()
            print(f"Book with ISBN {isbn} borrowed successfully.")
        else:
            print(f"Book with ISBN {isbn} is currently unavailable.")
    else:
        print(f"Error: Book with ISBN {isbn} not found.")
    print("")

# Function to return a borrowed book
def return_book():
    isbn = input("Enter ISBN : ")
    cursor.execute('''SELECT is_available FROM Book WHERE isbn = ?''', (isbn,))
    book = cursor.fetchone()
    if book:
        if book[0] == 0:
            cursor.execute('''UPDATE Book
                              SET is_available = 1
                              WHERE isbn = ?''', (isbn,))
            conn.commit()
            print(f'Book with ISBN {isbn} returned successfully.')
        else:
            print(f'Error: Book with ISBN {isbn} was not borrowed.')
    else:
        print(f'Error: Book with ISBN {isbn} not found.')
    print("")

# Function to view all available books
def view_available_books():
    cursor.execute('''SELECT isbn, book_title, author, publication_year FROM Book WHERE is_available = 1''')
    books = cursor.fetchall()
    if books:
        print('Available Books:')
        for book in books:
            print(f'ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}')
    else:
        print('No books available.')
    print("")


#Functions
def Functions():
    is_continue = True
    while is_continue:
        print("Library Management System")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View available books")
        print("5. Exit")

        choice = int(input("Please, choose your requirements from above : "))

        if choice == 1:
            add_book()
        if choice == 2:
            borrow_book()
        if choice == 3:
            return_book()
        if choice == 4:
            view_available_books()
        if choice == 5:
            print("Thank you, Visit again")
            # is_continue = False
        else:
            print("Please enter valid choice!!")

Functions()

# Close connection
conn.close()
