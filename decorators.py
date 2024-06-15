def greet(fx):
    def newfx():
        print("hi!! Good Morning")
        fx()
        print("Ok!! Good Night")
    return newfx
 
def greet1(fx):
    def newfx(*args,**kwargs):
        print("Sum is: ")
        fx(*args,**kwargs)
        print("Final answer")
    return newfx
#@greet     
def Name():
    print("My name is Eman")

#@greet1  
def add(a,b):
    print(f"{a+b}")  
#Name()
greet1(add)(3,4)
greet(Name)()