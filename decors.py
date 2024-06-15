def greet(func):
    def newfunc(*args,**kwargs):
        print("Assalam o Alaikum")
        func(*args,**kwargs)
        print("Apka Bohot Shukriya!!")
    return newfunc

def Sum(a,b):
    print(f"Apka jawab {a+b} ha")
    
greet(Sum)(2,3)