num = (input('Enter a number: '))
print(f"Multiplication table of {num} is")

try:
    for i in range(1, 11):
        print(f"{int(num)} X{int(i)} = {int(num*i)}")
except:
    print("Sorry some eroor")


print("Python programming")
print("Hello world")
