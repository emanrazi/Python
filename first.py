# FUNCTION TO PRINT THE SUM
'''
def sum_of_number(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

user_input = input("Enter the numbers by space: ")

nums = tuple(map(int, user_input.split()))
# Passing the tuple
c = sum_of_number(*nums)
print(c)

a=65
b='A'
print(chr(a))
print(ord(b))

print("Enter your name: ")
name=input()
print("My name is: ",name)

num1=input("Enter first Number: ")
num2=input("Enter second number: ")
print("Sum is = ",int(num1)+int(num2))

a="65"
print(chr(int(a)))
'''

name="Eman"
print("My name is: "+name)
#print(name[0]) #indexing

for character in name:
    print(character)
