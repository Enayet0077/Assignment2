class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__availability

    def borrow_book(self):
        if self.__availability:
            self.__availability=False

    def return_book(self):
        self.__availability=True

    def view_book_info(self):
        print(f"ID:{self.__book_id},Title:{self.__title},Author:{self.__author},Availability:{'Available'if self.__availability else 'Not Available'}")


class Library:
    book_list=[]

    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)


library = Library()
book1=Book(101,"Python Programming", "John Doe", True)
book2=Book(102,"Data Science Essentials", "Jane Smith", True)
book3=Book(103,"Machine Learning", "Alan Turing", True)
book4=Book(104,"Artificial Intelligence", "Marvin Minsky", True)
book5=Book(105,"Deep Learning", "Yann LeCun", True)
book6=Book(106,"Natural Language Processing", "Christopher Manning", True)
book7=Book(107,"Statistics for Data Science", "David C. Hsu", True)
book8=Book(108,"Python for Data Analysis", "Wes McKinney", True)

library.entry_book(book1)
library.entry_book(book2)
library.entry_book(book3)
library.entry_book(book4)
library.entry_book(book5)
library.entry_book(book6)
library.entry_book(book7)
library.entry_book(book8)

while True:
    print()
    print("-----> Welcome to the Library <-----")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    print()
    cmd=int(input("Enter your choice: "))
    print()

    if cmd ==1:
        print("Library Books:")
        for book in library.book_list:
            book.view_book_info()
    elif cmd==2:
        borrow_id=int(input("Enter the Book ID to borrow: "))
        print()
        found = False
        for book in library.book_list:
            if book._Book__book_id==borrow_id:
                found = True
                if book.is_available():
                    book.borrow_book()
                    print(f"Book '{book.get_title()}' borrowed successfully.")
                else:
                    print(f"Error 400 - Bad Request (Book is already borrowed)")
                break
        if not found:
            print(f"Error 400- Bad Request (Invalid Book ID)\nThere's no book with ID {borrow_id} in this library.")
    elif cmd==3:
        return_id=int(input("Enter the Book ID to return: "))
        print()
        found=False
        for book in library.book_list:
            if book._Book__book_id==return_id:
                found = True
                if not book.is_available():
                    book.return_book()
                    print(f"Book '{book.get_title()}'returned successfully.")
                else:
                    print(f"Error 400 - Bad Request (Book is already returned)")
                break
        if not found:
            print(f"Error 400 - Bad Request (Invalid Book ID)\nThere's no book with ID {return_id} in this library.")
    elif cmd == 4:
        print("Exiting the Library System...")
        break
    else:
        print("Invalid choice. Please try again.")
