class Math:
    @staticmethod
    #by using static method we can access the instance variable without using self as a parameter
    def PrintTable(num):
        for i in range(1,11):
            print(f"{num} X {i} = {num*i}")
    
m=Math()
num=int(input("Enter the no. for which u want to print a table: "))
m.PrintTable(num)