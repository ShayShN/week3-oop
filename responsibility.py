# class Book:
#     def __init__(self, title: str, author: str, content: str):
#         self.title = title
#         self.author = author
#         self.content = content
        
     
# class Libary:
#     def __init__(self):
#         self.list_saving = []
        
#     def save_to_list(self, filename):
#         self.list_saving.append(filename) 
        
# book1 = Book("Harry", "shay n", "king of jungle")
# saved = Libary()
# saved.save_to_list(book1.content)   
# print(saved.list_saving)

#2

# class Student:
#     def __init__(self, name: str, grades: list[int]):
#         self.name = name
#         self.grades = grades
        
            
# class GradeCalculator:
#     def __init__(self):
#            pass  
    
#     @staticmethod
#     def average_grade(grades):
#         return sum(grades) / len(grades) 

# s1 = Student("shay", [100, 85, 90])
# g = GradeCalculator()

# print(g.average_grade(s1.grades))

#3
# class Order:
#     def __init__(self, items: list[str], total_price: float):
#         self.items = items
#         self.total_price = total_price
    
    
    
# class InvoicePrinter:
#     def __init__(self):
#         pass
    
#     def print_invoice(self, order : Order):
#         print(f'items: {order.items} total_price: {order.total_price}')
        
# o = Order(["tost", "pizza"], 130.5)
# i = InvoicePrinter()

# i.print_invoice(o)   

##4

# from math import pi
# from abc import abstractmethod

# class Shape:
#     def __init__(self, type: str):
#         self.type = type
    
#     @abstractmethod    
#     def area(self):
#       pass  
        
            
    
# class Circle(Shape):
#     def __init__(self, type, r: int):
#         super().__init__(type)
#         self.r = r
        
#     def area(self):
#         return pi * (self.r * self.r)
       
         
# class Square(Shape):
#     def __init__(self, type, a: int):
#         super().__init__(type)
#         self.a = a
    
#     def area(self):  
#         return self.a * self.a 
         
# class Rectangle(Shape):
#     def __init__(self, type, a, b):
#         super().__init__(type)
#         self.a = a
#         self.b = b
        
     
#     def area(self):
#         return self.a * self.b 
    
# circle1 = Circle("circle", 4)
# square1 = Square("square", 20)
# rectangle1 = Rectangle("rectangle", 20, 30)

# shapes = [circle1, square1, rectangle1]
# for shape in shapes:
#     print(shape.area())


##5

# class Payment:
#     def __init__(self):
#         pass
    
#     def pay(self, amount):
#         print(amount)

# class CreditCardPayment(Payment):
#     def __init__(self):
#         pass
#     def pay(self, amount):
#         return super().pay(amount)
        
# class PayPalPayment(Payment):
#     def __init__(self):
#         pass
    
#     def pay(self, amount):
#         return super().pay(amount)
    
# class CryptoPayment(Payment):
#     def __init__(self):
#         pass

#     def pay(self, amount):
#         return super().pay(amount)

# c = CreditCardPayment()
# c.pay(222)

##6
# from abc import abstractmethod

# class Notifier:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def send(self, message):
#         pass


# class EmailNotifier(Notifier):
#     def __init__(self):
#         pass
        
#     def send(self, message):
#         pass


# class SMSNotifier(Notifier):
#     def __init__(self):
#         pass
    
#     def send(self, message):
#         pass

        
# class PushNotifier(Notifier):
#     def __init__(self):
#          pass
    
#     def send(self, message):
#         pass




##7

# class GroundUnit:
#     def __init__(self):
#         pass
    
    
# class FlyingUnit:
#     def __init__(self):
#         pass
    
#     def fly(self):
#         pass
    

# class Drone(FlyingUnit):
#     def __init__(self):
#         pass
    
#     def fly(self):
#         pass
    
    
# class Tank(GroundUnit):
#     def __init__(self):
#         pass
# #לציפור יש יכולת לעוף ולטנק אין    
    


##8
# from abc import abstractmethod

# class Soldier:
#     def __init__(self):
#         pass
  
    
# class Shooter:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def shoot(self):
#         pass
  
  
# class Navigator:
#     def __init__(self):
#         pass
       
#     @abstractmethod
#     def navigate(self):
#         pass


# class AirSupportCaller:
#     def __init__(self):
#         pass
        
#     @abstractmethod
#     def callAirSupport(self):
#         pass


# class Infantry(Shooter, Navigator):
#     def __init__(self):
#         pass
    
#     def shoot(self):
#         pass
    
#     def navigate(self):
#         pass
    

# class ForwardObserver(Shooter, AirSupportCaller):
#     def __init__(self):
#         pass
    
#     def shoot(self):
#         pass
    
#     def callAirSupport(self):
#         pass
 

# class Pilot(AirSupportCaller):
#     def __init__(self):
#         pass
    
#     def callAirSupport(self):
#         pass 
# # אבסטרקט מאלץ שימוש ,חילקתי ל CLASS קטנים יותר שאפשר יהיה לרשת ,למשל חיל רגלים יכול רק לירות ולנווט     

##9
# from abc import abstractmethod

# class IDrive:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def drive(self):
#         pass    

# class IFly:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def fly(self):
#         pass


# class ISail:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def sail(self):
#         pass


# class Tank(IDrive):
#     def __init__(self):
#         pass
    
#     def drive(self):
#         pass

# class FighterJet(IFly, IDrive):
#     def __init__(self):
#         pass

#     def fly(self):
#         pass

#     def drive(self):
#         pass
    

# class Submarine(ISail):
#     def __init__(self):
#         pass
    
#     def sail(self):
#         pass
# # לרשת אבסטרקט כשהוא לא צריך את התכונה ,חילקתי לקלאסים שונים וקטנים


##10
# from abc import abstractmethod

# class RadioComm:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def sendRadio(self):
#         pass


# class  SatelliteComm:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def sendSatellite(self):
#         pass
    

# class MorseComm:
#     def __init__(self):
#         pass
    
#     @abstractmethod
#     def sendMorseCode(self):
#         pass
    
    
# class FieldRadio(RadioComm):
#     def __init__(self):
#         pass
#     def sendRadio(self):
#         pass
    
# class SatelliteComm(SatelliteComm):
#     def __init__(self):
#         pass
#     def sendSatellite(self):
#         pass
    
# class LegacyMorseUnit(MorseComm):
#     def __init__(self):
#         pass
#     def sendMorseCode(self):
#         pass
# # פיצלתי מחלקות בכדי שכולם יוכלו להשתמש    
























