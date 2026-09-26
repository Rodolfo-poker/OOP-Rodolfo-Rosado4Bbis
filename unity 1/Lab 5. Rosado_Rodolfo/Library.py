class library:
    def __init__(self):
        self.users = []
        self.books = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            print(book.show_book_info())
    
    def find_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                return book
        return None
    
    def find_user(self, id_user):
        for user in self.users:
            if user.id == id_user:
                return user
        return None
    
    def borrow_book(self, id_book, id_user):
        book = self.find_book(id_book)
        user = self.find_user(id_user)
        
        if book is None or user is None:
            print("Book or user not found")
            return
        
        if not book.available:
            print(f"The book '{book.title}' is already borrowed")
            return
        
        book.available = False
        user.borrowed_books.append(book)
        print(f"{user.name} borrowed '{book.title}'")
    
    def return_book(self, id_book, id_user):
        book = self.find_book(id_book)
        user = self.find_user(id_user)
        
        if book is None or user is None:
            print("Book or user not found")
            return
        
        if book not in user.borrowed_books:
            print(f"{user.name} does not have this book borrowed")
            return
        
        book.available = True
        user.borrowed_books.remove(book)
        print(f"{user.name} returned '{book.title}'")