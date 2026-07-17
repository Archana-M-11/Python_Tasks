class FineCalculationDecorator:

    def borrow_book(self, member, book):
        member.borrow_book(book)
        print("Fine calculation completed.")
class EmailNotificationDecorator:

    def borrow_book(self, member, book):
        member.borrow_book(book)
        print("Email notification sent.")

class LoggingDecorator:

    def borrow_book(self, member, book):
        member.borrow_book(book)
        print("Borrow operation logged.")