from library_package.book import Book
from library_package.member import Member
from library_package.library import Library
from library_package.librarian import Librarian
from library_package.search_strategy import SearchByTitle, SearchByAuthor, SearchByCategory, SearchByISBN
from library_package.decorators import FineCalculationDecorator, EmailNotificationDecorator, LoggingDecorator
from library_package.exceptions import BookNotFoundException, MemberNotFoundException

library = Library.get_instance()

librarian = Librarian('L101', 'Anu')

book1 = Book('B101', 'Python Programming', 'Guido', 'Programming', 'ISBN101', 2024, 5, 5)
book2 = Book('B102', 'Django Basics', 'Adrian', 'Programming', 'ISBN102', 2023, 3, 3)

librarian.add_book(library, book1)
librarian.add_book(library, book2)

print('Books added successfully.\n')

member1 = Member('M101', 'Archana', 'archana@gmail.com', '9876543210', 'Gold')
member2 = Member('M102', 'Rahul', 'rahul@gmail.com', '9876543211', 'Silver')

librarian.register_member(library, member1)
librarian.register_member(library, member2)

print('Members registered successfully.\n')

member1.borrow_book(book1)
print('Book borrowed successfully.\n')

print('Borrowed Books:')
member1.view_borrowed_books()
print()

member1.return_book(book1)
print('Book returned successfully.\n')

print('Search By Title:')
books = library.search_books(SearchByTitle(), 'Python')
for book in books:
    print(book)

print()

print('Search By Author:')
books = library.search_books(SearchByAuthor(), 'Guido')
for book in books:
    print(book)

print()

print('Search By Category:')
books = library.search_books(SearchByCategory(), 'Programming')
for book in books:
    print(book)

print()

print('Search By ISBN:')
books = library.search_books(SearchByISBN(), 'ISBN102')
for book in books:
    print(book)

print()

print('Decorator Testing:')

fine = FineCalculationDecorator()
fine.borrow_book(member2, book2)
member2.return_book(book2)

email = EmailNotificationDecorator()
email.borrow_book(member2, book2)
member2.return_book(book2)

log = LoggingDecorator()
log.borrow_book(member2, book2)

print()

print('Exception Testing:')

try:
    librarian.remove_book(library, 'B999')
except BookNotFoundException as e:
    print(e)

try:
    librarian.remove_member(library, 'M999')
except MemberNotFoundException as e:
    print(e)