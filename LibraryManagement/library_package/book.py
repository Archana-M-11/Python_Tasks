from library_package.exceptions import BookUnavailableException

class Book:
    def __init__(self, book_id, title, author, category, isbn,
                 publication_year, total_copies, available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__category = category
        self.__isbn = isbn
        self.__publication_year = publication_year
        self.__total_copies = total_copies
        self.__available_copies = available_copies
    
    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_category(self):
        return self.__category

    def get_isbn(self):
        return self.__isbn

    def get_publication_year(self):
        return self.__publication_year

    def get_total_copies(self):
        return self.__total_copies

    def get_available_copies(self):
        return self.__available_copies
    
    def borrow_book(self):
        if self.__available_copies >0:
            self.__available_copies-=1
        else:
            raise BookUnavailableException('Book is not available ')
        
    def return_book(self):
        if self.__available_copies < self.__total_copies:
            self.__available_copies+=1
    
    def if_available(self):
        if self.__available_copies > 0:
            return True
        return False
    
    def display_book_details(self):
        print('Book ID :',self.__book_id)
        print('Title :',self.__title)
        print('Author :',self.__author)
        print('Category :',self.__category)
        print('ISBN :',self.__isbn)
        print('Publication Year :',self.__publication_year)
        print('Total Copies :',self.__total_copies)
        print('Available Copies :',self.__available_copies)

    def __str__(self):
        return (f"Book ID: {self.__book_id}, "
            f"Title: {self.__title}, "
            f"Author: {self.__author}, "
            f"Category: {self.__category}, "
            f"ISBN: {self.__isbn}, "
            f"Publication Year: {self.__publication_year}, "
            f"Total Copies: {self.__total_copies}, "
            f"Available Copies: {self.__available_copies}")
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.__book_id == other.__book_id
        return False