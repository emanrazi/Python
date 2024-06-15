def Sum(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

tup=()
temp=list(tup)
while True:
    num=int(input("Enter a number: "))
    if(num==-1):
        break
    temp.append(num)
    
tup=tuple(temp)
result=Sum(*tup)
print("Sum is = ",result)