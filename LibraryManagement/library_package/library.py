from library_package.exceptions import (BookNotFoundException,MemberNotFoundException)
from library_package.search_strategy import SearchStrategy

class Library:
    __instance = None
    def __init__(self):
        if Library.__instance is not None:
            raise Exception('Only one Library object can be created.')
        self.__books = []
        self.__members = []
        Library.__instance = self
    
    @staticmethod
    def get_instance():
        if Library.__instance is None:
            Library()
        return Library.__instance
    
    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id:
                self.__books.remove(book)
                return
        raise BookNotFoundException("Book not found.")
    
    def update_book(self, book_id, updated_book):
        for i, book in enumerate(self.__books):
            if book.get_book_id() == book_id:
                self.__books[i] = updated_book
                return
        raise BookNotFoundException("Book not found.")
    def register_member(self, member):
        self.__members.append(member)

    def remove_member(self, member_id):
        for member in self.__members:
            if member.get_member_id() == member_id:
                self.__members.remove(member)
                return
        raise MemberNotFoundException("Member not found.")
        
    def search_books(self, search_strategy, keyword):
        return search_strategy.search(self.__books, keyword)
    

