class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
       return f'x: {self.x} y: {self.y}'
        

class Line:
    
    count = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Line.count += 1
        
    def show(self):
        print(self.a, self.b)
    
        
    @classmethod     
    def how_many(cls):
        print(cls.count)
    
    @staticmethod    
    def is_horizontal(line):
        return line.a.y == line.b.y
    
    @staticmethod
    def is_vertical (line):
        return line.a.x == line.b.x
    
if __name__=="__main__":  
    p1 = Point(5, 9)
    p2 = Point(8, 9)
    line1 = Line(p1, p2) 

    line1.show()    
    line1.how_many()
    print(Line.is_horizontal(line1))
    print(Line.is_vertical(line1))    
        
        
        
    
        
