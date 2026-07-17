class Member:
    def __init__(self, member_id, name, email, phone, membership_type):
        self.__member_id = member_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__membership_type = membership_type
        self.__borrowed_books = []
    
    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_membership_type(self):
        return self.__membership_type

    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def borrow_book(self, book):
         book.borrow_book()
         self.__borrowed_books.append(book)
    
    def return_book(self,book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
    
    def view_borrowed_books(self):
        if not self.__borrowed_books:
           print("No books borrowed.")
        else:
             for book in self.__borrowed_books:
                print(book.get_title())

    def display_member(self):
        print('Member ID :', self.__member_id)
        print('Name :', self.__name)
        print('Email :', self.__email)
        print('Phone :', self.__phone)
        print('Membership Type :', self.__membership_type)
        print('Borrowed Books :')
        if not self.__borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.__borrowed_books:
             print(book.get_title())