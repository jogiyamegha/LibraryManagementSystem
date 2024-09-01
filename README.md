Library Management System

This simple application created using Python, with SQLite as the database to handle the backend data storage. The system supports basic library operations, such as adding books, borrowing books, returning books, and viewing the list of available books.

Features :
Database and Table Structure:

The system uses SQLite, a lightweight database, to store data persistently.
A single table called Book is created in the database to store details of the books. Each record in the table represents a book with attributes like title, author, publication year and availability status.

Adding Books:
When a new book is added, the system checks if the book already exists in the database. If the book is already present, the system prevents duplicate entries, ensuring that each book is unique in the database.
If the book is not already present, it is added to the Book table with its relevant details.

Borrowing Books:
Users can borrow a book from the library. The system checks if the requested book is available (i.e., it hasn’t been borrowed by someone else).
If the book is available, the system updates the book’s status to indicate it has been borrowed, ensuring that it can't be borrowed by another user until it is returned.

Returning Books:
Users can return a borrowed book. Once returned, the system updates the book's status to available, allowing other users to borrow it.

Viewing Available Books:
Users can view a list of all available books in the library. The system queries the Book table and filters out the books that are currently borrowed.

Error Handling
The system includes error handling mechanisms, such as checking for duplicate entries when adding books and ensuring that a book is available before it can be borrowed. This helps maintain the integrity of the database and ensures smooth operation of the system.
