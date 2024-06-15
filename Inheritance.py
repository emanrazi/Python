class Persson:
    def __init__(self,id,name,address,phone_no):
        self._id=id
        self._name=name
        self._address=address
        self._phone_no=phone_no

class Employee(Persson):
    def __init__(self,id,name,address,phone_no,dob):
        self._id=id
        self._name=name
        self._address=address
        self._phone_no=phone_no
        self.dob=dob
    
    def Show(self):
        print(f"Employee id is: {self._id}")
        print(f"Employee Name is: {self._name}")
        print(f"Employee adress is: {self._address}")
        print(f"Employee dob is: {self.dob}")
        print(f"Employee phoneNo is: {self._phone_no}")
        
emp=Employee(11,"Asad","Gujrat","123455-33","12-01-2001")
emp.Show()