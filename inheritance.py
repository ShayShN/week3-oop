# class Vehicles:
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("The vehicle is moving")  
          
#     def __str__(self):
#         return f'brand: {self.brand}, model: {self.model}'
    
# class Car(Vehicles):
#     def move(self):
#         return "the car drives"
        
# class Plane(Vehicles):
#     def move(self):
#         return "the plane flies"
        
# vehicle = Vehicles("toyota", "corola")
# vehicle.move()
# car = Car("toyota", "corola")
# plane = Plane("Air force", "Hercoles")

# print(car.move())
# print(plane.move())

#2    
# class Animals:
#    def sound(self):
#         return "sounds"
    
# class Dog(Animals):
#     def sound(self):
#         return "Woof"
    
# class Cat(Animals):
#     def sound(self):
#         return "Meow"
    
# animals = [Dog("rex"), Dog("Jeck"), Cat("mitsi")]
# for i in animals:
#     print(i.sound())

#3
# class Shape:
#     def __init__(self, name):
#         self.name = name
        
#     def area(self):
#         raise NotImplementedError
    
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.name = name
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height
                
        
        
