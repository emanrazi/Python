def Sum( a, b):
    {
        print("SUm is = ",a+b)
    }

def Subtract(a,b):
    {
        print("Subtract = ",a-b)
    }

def Multiply(a,b):
    {
        print("Multiplication = ",a*b)
    }
   
def Divide(a,b):
    {
        print("Divison = ",a/b)
    } 
print("1. Sum")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
x=int(input("ENter your choice: "))
num1=int(input("Enter first number: "))
num2=int(input("Enter 2nd number: "))
match x:
    case 1:
        Sum(num1,num2)
    case 2:
       Subtract(num1,num2)
    case 3:
        Multiply(num1,num2)
    case 4:
        Divide(num1,num2)
    case _:
        print("Invalid Choice")
        