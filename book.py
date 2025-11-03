from tarfile import NUL


class Book:

    def __init__(self, id, title, author, is_available=True):
        self._id = id
        self._title = title
        self._author = author
        self._is_available = is_available
        
    def unavailable_mark(self):
        if self._is_available:
            self._is_available = False
    
    def available_mark(self):
        self._is_available = True
        
class Member:
    def __init__(self, id, full_name, active_loans_count=0):
        self._id = id
        self._full_name = full_name
        self._active_loans_count = active_loans_count
    
    def loans_increment(self):
        self._active_loans_count += 1
         
    def loans_decrement(self):
        if self._active_loans_count > 0:
            self._active_loans_count -= 1
    

class Loan:
    def __init__(self, loan_id, book_id, member_id,  open_date, return_date=NUL, status="Open"):
        self._loan_id = loan_id
        self._book_id = book_id
        self._member_id = member_id
        self._status = status
        self._open_date = open_date
        self._return_date = return_date 
    
    def closed(self):
        if self._status == "Open":
            self._status = "Closed"       


class Libary:           
    def __init__(self):
        self._collections = []
        
    def add_book(self, book):
        self._collections.append(book)  
        
    def add_member(self, member):
        self._collections.append(member)
        
    def borrow(self, book_id, member_id, date):
        
             