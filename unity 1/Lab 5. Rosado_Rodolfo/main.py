from Books import book
from Users import user
from Library import library

book1 = book("001", "OOP Fundamentals", "Jhon Lennon", "BBC")
book2 = book("002", "Python for Dummies", "Stef Maruzh", "For Dummies")

user1 = user("001", "Said Vara", "1234")

library = library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.show_books()

library.borrow_book("001", "001")
library.borrow_book("001", "001")

library.return_book("001", "001")
library.borrow_book("001", "001")