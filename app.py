from turtle import width


class BankAccoount:
    def __init__(self, account_number, balance):
        self. account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            
    def get_balance(self):
        return self.balance
   
   
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 *(self.width + self.height)   
    
class Student:
    def __init__(self, name, grades=[int]):
        self.name = name
        self.grades = grades
        
    def add_grade(self, grade):
        self.grades += grade
            
    def average(self):
        return self.grades
    
class Book:
    def __init__(self, title, author, pages, is_read: bool):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False
    
    def mark_as_read(self):
        self.is_read = True
    
    def info(self):
        print(self.title)
        
class Counter:
    def __init__(self, count=0):
        self.count = count
    
    def increase(self):
          
            
