class Author:
    def __init__(self, author_name):
        self.__author_name = author_name

    def get_author_name(self):
        return self.__author_name

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def __str__(self):
        return f"Author Name    : {self.__author_name}"

class Publisher:
    def __init__(self, publisher_name):
        self.__publisher_name = publisher_name

    def get_publisher_name(self):
        return self.__publisher_name

    def set_publisher_name(self, publisher_name):
        self.__publisher_name = publisher_name

    def __str__(self):
        return f"Publisher Name : {self.__publisher_name}"


class Book(Author, Publisher):
    def __init__(self, author_name, publisher_name, book_title, price):
        Author.__init__(self, author_name)
        Publisher.__init__(self, publisher_name)

        self.__book_title = book_title
        self.__price = price

    def get_book_title(self):
        return self.__book_title

    def get_price(self):
        return self.__price

    def set_book_title(self, title):
        self.__book_title = title

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Invalid Price!")

    def __str__(self):
        return (
            Author.__str__(self)
            + "\n"
            + Publisher.__str__(self)
            + f"\nBook Title     : {self.__book_title}"
            + f"\nPrice          : Rs.{self.__price}"
        )

book1 = Book(
    "James Clear",
    "Penguin Books",
    "Atomic Habits",
    1500
)

print("Book Details")
print(book1)

book1.set_price(1800)
book1.set_book_title("Atomic Habits (Updated Edition)")

print("\nAfter Updating Details")
print(book1)