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

view_available_books()
conn.close()