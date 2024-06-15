class Student:
    def __init__(self,id,name,address,dob):
        # i will create private attributes
        self.__id=id
        self.__name=name #declare it as protected
        self.__address=address
        self.__dob=dob
        #i will declare the method as private
    def __display(self):
        print(f"My id is {self.__id}")
        print(f"My name is {self.__name}")
        print(f"I am from {self.__address}")
        print(f"My date of birth is {self.__dob}")
    #### GETTER AND SETTERS
    def get_Name(self):
        return self.__name
    def set_Name(self,name):
        self.__name=name
        
    def get_Address(self):
        return self.__address
    def set_Address(self,address):
        self.__address=address
        
    def get_Id(self):
        return self.__id
    def set_Id(self,id):
        self.__id=id 

#class Branch(Student):
    def show(self):
        print(f"My name is {self._name}")
    
st=Student(1,"Eman","Gujrat","12-09-2002")
st.set_Id(22)
st.set_Name("Ali")
st.set_Address("Islamabad")

print(f"My id is {st.get_Id()}")
print(f"My name is {st.get_Name()}")
print(f"I am from {st.get_Address()}")


#st.display()
#alternate method to access private methods or class

#st._Student__display()
#br=Branch(1,"Eman","Gujrat","12-09-2002")
#br.show()