class Shape:
    def __init__(self,len,width):
        self.len=len
        self.width=width
    
    def area(self):
        return self.len*self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius) #provide parameters to parent class to initialize it
    
    def area(self):
        super().area()
        return 3.14*self.radius*self.radius
        #return 3.14*super().area()
 
c=Circle(2)
print(f"Area of Circle is: {c.area()}") 
      
rec=Shape(3,4)
print(f"Area of Rectangle is: {rec.area()}")    
