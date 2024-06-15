def Recursion(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*Recursion(num-1)

num=int(input("Eneter a number to find factorial: "))
num=Recursion(num)

print("FActorial is: ",num)