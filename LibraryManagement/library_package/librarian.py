class Librarian:
    def __init__(self, librarian_id, name):
        self.__librarian_id = librarian_id
        self.__name = name

    def get_librarian_id(self):
        return self.__librarian_id

    def get_name(self):
        return self.__name
    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)

    def update_book(self, library, book_id, updated_book):
        library.update_book(book_id, updated_book)

    def register_member(self, library, member):
        library.register_member(member)

    def remove_member(self, library, member_id):
        library.remove_member(member_id)