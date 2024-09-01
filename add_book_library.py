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

def add_book(id,isbn, book_title, author, publication_year, is_available):
    try:
        cursor.execute('''INSERT INTO Book (id, isbn, book_title, author, publication_year, is_available)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (id, isbn, book_title, author, publication_year, is_available))
        conn.commit()
        print(f"Book '{book_title}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"ERROR: Book with ISBN {isbn} already exists.")
    print("")

# Test the functions
add_book(1, '978-0132350884', 'Clean Code', 'Robert C. Martin', 2008, 1)
add_book(2, '972-0132350885', 'Saurashtra ni rasdhar', 'Zaverchand Meghani', 2009, 1)
add_book(3, '971-0132350886', 'Humfala Avsar', 'Dr I K Vijliwala', 2012, 1)
add_book(4, '9711-0132350887', 'The puzzled!', 'Dr I K Vijliwala', 2022, 1)
add_book(5, '923-0132350889', 'Malela jeev', 'Pannalal Patel', 1941, 1)
add_book(6, '9008-0132350890', 'Saraswatichandra', 'Goverdhanram Tripathi', 1887, 1)
add_book(7, '990098-0132350891', 'Prithvivallabh', 'K M Munshi', 1921, 1)
add_book(8, '9232-0132350892', 'Mansai na diva', 'Zaverchand Meghani', 1953, 1)
add_book(9, '9702-0132350893', 'Manvi ni bhavai', 'Pannalal Patel', 1941, 1)
add_book(10, '990098-013291', 'Othar', 'Ashwini Bhatt', 1984, 1)
add_book(11, '9232-02350892', 'Samundarantike', 'Dhruv Bhatt', 1993, 1)
add_book(12, '9702-01378950893', 'Madhyabindu', 'Kaajal Oza Vaidya', 2007, 1)
add_book(13, '97-01378950893', 'Madhya', 'Kaajal Oza Vaidya', 2007, 1)
conn.close()
