import logging
from abc import ABC, abstractmethod

logger = logging.getLogger("library_manager")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler("library.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)
logger.addHandler(fh)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f"Book removed: {title}")
                return
        logger.warning(f"Attempted to remove non-existent book: {title}")

    def get_books(self):
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f'Book "{title}" added successfully.')

    def remove_book(self, title):
        self.library.remove_book(title)
        print(f'Book "{title}" removed successfully (if it existed).')

    def show_books(self):
        books = self.library.get_books()
        if books:
            print("Books in the library:")
            for book in books:
                print(book)
        else:
            print("The library is empty.")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
