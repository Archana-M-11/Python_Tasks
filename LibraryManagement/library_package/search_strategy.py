class SearchStrategy:
    def search(self, books, keyword):
        pass
    
class SearchByTitle(SearchStrategy):
    def search(self, books, keyword):
        result = []

        for book in books:
            if keyword.lower() in book.get_title().lower():
                result.append(book)

        return result


class SearchByAuthor(SearchStrategy):
    def search(self, books, keyword):
        result = []

        for book in books:
            if keyword.lower() in book.get_author().lower():
                result.append(book)

        return result


class SearchByCategory(SearchStrategy):
    def search(self, books, keyword):
        result = []

        for book in books:
            if keyword.lower() in book.get_category().lower():
                result.append(book)

        return result


class SearchByISBN(SearchStrategy):
    def search(self, books, keyword):
        result = []

        for book in books:
            if book.get_isbn() == keyword:
                result.append(book)

        return result