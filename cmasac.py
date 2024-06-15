#Class methods as ALTERNATIVE CONSTRUCTORS
class Employee:
    def __init__(self,id,name,address,salary):
        self.id=id
        self.name=name
        self.address=address
        self.salary=salary
      
    @classmethod  
    def change(self,str):
        employee=str.split("-")
        return self(employee[0],employee[1],employee[2],employee[3])
    
emp=Employee(1,"Eman","Gujrat",50000)
print(f"Employee name is: {emp.name}")

emp2=Employee.change("1-Ali-Gujrat-345600")
print(f"Employee name is: {emp2.name}")
print(f"Employee salary is: {emp2.salary}")