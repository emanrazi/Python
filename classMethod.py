class Employee:
    #class variable
    company="Apple"
    def __init__(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address
    
    @classmethod
    #by defining the classmethod we can change the actual/initial value of class variable
    def change(self,company_name):
        self.company=company_name
        
e1=Employee(1,"Ali","Gujrat")
print(f"Employee id is: {e1.id}")
print(f"Employee name is: {e1.name}")
print(f"Employee address is: {e1.address}")
print(f"Employee company is: {e1.company}")

e2=Employee(2,"Eman","Gujrat")
e2.change("Apple Advance")
print(f"Employee id = {e2.id}")
print(f"Employee name = {e2.name}")
print(f"Employee address = {e2.address}")
print(f"Company name is: {e2.company}")

print(f"Company name after changing is: {e1.company}")

        
    
    
        
        