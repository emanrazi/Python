class Human:
    def __init__(self,heart):
        print("HUman constructor is called")
        self.heart=heart
        self.no_eyes=2
        self.no_nose=1
    def eat(self):
        print("I can eat")
        
    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        print("Male connstructor is called")
        self.name=name
    def flirt(self):
        print("I can flirt")
        
    def work(self):
        print("I can code")

class boy(Human,Male):
    def __init__(self,name,heart):
        Male.__init__(self,name)
        Human.__init__(self,heart)
    def work(self):
        print("I can both work and code")
        

b=boy("Eman",1)
#print(f"My name is: {b.name}")
print(f"No. of heart is: {b.heart}")
#b=boy("Eman","English")
#b.work()
#m=Male("Eman")
#Male.work(b)
#print(b.no_nose)
#print(b.name)
#print(m.name)
#print(boy.mro())