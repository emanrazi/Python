class Employee:
    def __init__(self,id,name,country,dob):
        self.id=id
        self.name=name
        self.country=country
        self.dob=dob
    
emp=Employee(1,"Ali","Pakistan","11-02-2001")
print(f"Employee id is: {emp.id}")
print(f"Employee name is: {emp.name}")
print(f"Employee country is: {emp.country}")
print(f"Employee date of birth is: {emp.dob}")