class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        
    #operator overloading for adding
    def __add__(self,other):
        return (f"{self.real+other.real} + {self.imaginary+other.imaginary}i")
        
c1=Complex(1,2)
c2=Complex(3,4)
print(f"Sum of two complex no. is = {c1+c2}")