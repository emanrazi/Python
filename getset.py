class Employee:
    #class variables
    emp_id=0
    emp_name='0'
    emp_cnic='0'
    def setId(self,id):
        self.emp_id=id
        
    def setName(self,name):
       self. emp_name=name
    
    def setCNIC(self,cnic):
        self.emp_cnic=cnic
        
    def getId(self):
        return self.emp_id
    
    def getName(self):
        return self.emp_name
    
    def getCNIC(self):
        return self.emp_cnic
    

emp=Employee()
emp.setId(1)
emp.setName("Eman")
emp.setCNIC("34201-123456")
print("Employee id is = ",emp.getId())
print("Employee Name is = ",emp.getName())
print("Employee CNIC is = ",emp.getCNIC())