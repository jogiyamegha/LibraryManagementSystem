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

def borrow_book(isbn):
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


borrow_book('923-0132350889')
borrow_book('9232-0132350892')
conn.close()