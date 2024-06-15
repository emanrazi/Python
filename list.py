def Sum(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

numbers=[]
while True:
    
    num=int(input("Enter a number: "))
    if(num==-1):
        break
    numbers.append(num)

r=Sum(*numbers)
print("Sum is = ",r)