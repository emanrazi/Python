class A:
    def Parent(self):
        print("This is parent method of Class A")
        
class B(A):
    #method overriding
    def Parent(self):
        print("This is parent method of Class B")
        #if u want to call the parent method of class A
        super().Parent()
    def Child(self):
        print("This is child method of class B")
    
b=B()
b.Parent()