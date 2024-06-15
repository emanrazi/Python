print("Enter 1st number: ")
val1=(input())
print("Enter 2nd number: ")
val2=(input())

def function(value1,value2):
    print("Sum is = ",value1+value2)
    
def myName():
    print("My name is Eman")
try:
    function(int(val1),int(val2))
except Exception as e:
    print(e)
finally:
    myName()
    
        
    