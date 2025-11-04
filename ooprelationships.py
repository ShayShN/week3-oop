# class Vehicles:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
    
#     def drive(self):
#         print(self.max_speed)    
    
    
# class Car(Vehicles):
#     pass
    
    
# class Motorcycle(Vehicles):
#     pass
    

# c = Car(100)        
# c.drive()



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
# class Manager(Employee):
#     def manage(self):
#         print(f'salary: {self.salary}\n manage: {self.name}')
    
# class Developer(Employee):
#     def write_code(self):
#         print("write code")
        
# m = Manager("shay", 60000)
# m.manage()

# d = Developer("shay", 10000000)
# d.write_code()



# from abc import  abstractmethod

# from math import pi
# class Shape:
#     @abstractmethod
#     def area():
#         pass

# class Rectangle(Shape):
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
     
#     def area(self):
#         return self.height * self.base

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return f'surface: {pi * (self.radius * self.radius)}'
        
# c = Circle(4)
# print(c.area())        
        

# class Square(Shape):
#     def __init__(self, height):
#         self.height = height
    
#     def area(self):
#         return self.height * self.height
        
        

 
        
        
             
     