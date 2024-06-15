import os
import time
import sys

# ANSI codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
temp = 1
flip_used = False
fifty_fifty_used = False
count = 1
List = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Press Enter to continue...")

def Winning_Amount(*List):
    total_amount = sum(List)
    print(YELLOW, "Total Amount you win =", total_amount, "$")

def Display():
    global count
    print(GREEN, "-------------------------------------------")
    print(GREEN, "-                                         -")
    print(YELLOW, "            QUESTION ", count)
    print(GREEN, "-                                         -")
    print(GREEN, "-------------------------------------------")
    count += 1

def List1(l1):
    if l1 == 3:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def List6(l6):
    if l6 == 2:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def List2(l2):
    if l2 == 2:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def List3(l3):
    if l3 == 3:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def List4(l4):
    if l4 == 1:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def List5(l5):
    if l5 == 4:
        print(YELLOW, "Congratulation! You win 50$")
        List.append(50)
    else:
        print(RED, "Wrong Answer, GAME OVER!")
        Winning_Amount(*List)
        sys.exit()

def Display_List1():
    global fifty_fifty_used
    global flip_used
    l1 = int(input())
    if l1 == 1 or l1 == 2 or l1 == 3 or l1 == 4:
        List1(l1)
    elif l1 == 6:
        if fifty_fifty_used:
            print("You have already used 50-50")
            Display_List1()
        else:
            fifty_fifty_used = True
            del list1[2]
            del list1[1]
            for i in list1:
                print(i)
            l1 = int(input())
            List1(l1)
    elif l1 == 5:
        if flip_used:
            print("You have already used FLIP")
            Display_List1()
        else:
            flip_used = True
            for i in list6:
                print(i)
            print("6. 50-50")
            l1 = int(input())
            if l1 == 6:
                if fifty_fifty_used:
                    print("You have already used 50-50")
                    Display_List1()
                else:
                    fifty_fifty_used = True
                    del list6[1]
                    del list6[3]
                    for i in list6:
                        print(i)
                    l1 = int(input())
                   
            List6(l1)

def Display_List2():
    global fifty_fifty_used
    global flip_used
    l2 = int(input())
    if l2 == 1 or l2 == 2 or l2 == 3 or l2 == 4:
        List2(l2)
    elif l2 == 6:
        if fifty_fifty_used:
            print("You have already used 50-50")
            Display_List2()
        else:
            fifty_fifty_used = True
            del list2[1]
            del list2[3]
            for i in list2:
                print(i)
            l2 = int(input())
            List2(l2)
    elif l2 == 5:
        if flip_used:
            print("You have already used FLIP")
            Display_List2()
        else:
            flip_used = True
            for i in list6:
                print(i)
            print("6. 50-50")
            l2 = int(input())
            if l2 == 6:
                if fifty_fifty_used:
                    print("You have already used 50-50")
                    Display_List2()
                else:
                    fifty_fifty_used = True
                    del list6[1]
                    del list6[3]
                    for i in list6:
                        print(i)
                    l2 = int(input())
                    
            List6(l2)

def Display_List3():
    global fifty_fifty_used
    global flip_used
    l3 = int(input())
    if l3 == 1 or l3 == 2 or l3 == 3 or l3 == 4:
        List3(l3)
    elif l3 == 6:
        if fifty_fifty_used:
            print("You have already used 50-50")
            Display_List3()
        else:
            fifty_fifty_used = True
            del list3[4]
            del list3[1]
            for i in list3:
                print(i)
            l3 = int(input())
            List3(l3)
    elif l3 == 5:
        if flip_used:
            print("You have already used FLIP")
            Display_List3()
        else:
            flip_used = True
            for i in list6:
                print(i)
            print("6. 50-50")
            l3 = int(input())
            if l3 == 6:
                if fifty_fifty_used:
                    print("You have already used 50-50")
                    Display_List3()
                else:
                    fifty_fifty_used = True
                    del list6[1]
                    del list6[3]
                    for i in list6:
                        print(i)
                    l3 = int(input())
                    
            List6(l3)
                    
def Display_List4():
    global fifty_fifty_used
    global flip_used
    l4 = int(input())
    if l4 == 1 or l4 == 2 or l4 == 3 or l4 == 4:
        List4(l4)
    elif l4 == 6:
        if fifty_fifty_used:
            print("You have already used 50-50")
            Display_List4()
        else:
            fifty_fifty_used = True
            del list4[4]
            del list4[3]
            for i in list4:
                print(i)
            l4 = int(input())
            List4(l4)
    elif l4 == 5:
        if flip_used:
            print("You have already used FLIP")
            Display_List4()
        else:
            flip_used = True
            for i in list6:
                print(i)
            print("6. 50-50")
            l4 = int(input())
            if l4 == 6:
                if fifty_fifty_used:
                    print("You have already used 50-50")
                    Display_List4()
                else:
                    fifty_fifty_used = True
                    del list6[1]
                    del list6[3]
                    for i in list6:
                        print(i)
                    l4 = int(input())
                    
            List6(l4)

def Display_List5():
    global fifty_fifty_used
    global flip_used
    l5 = int(input())
    if l5 == 1 or l5 == 2 or l5 == 3 or l5 == 4:
        List5(l5)
    elif l5 == 6:
        if fifty_fifty_used:
            print("You have already used 50-50")
            Display_List5()
        else:
            fifty_fifty_used = True
            del list5[1]
            del list5[2]
            for i in list5:
                print(i)
            l5 = int(input())
            List5(l5)
    elif l5 == 5:
        if flip_used:
            print("You have already used FLIP")
            Display_List5()
        else:
            flip_used = True
            for i in list5:
                print(i)
            print("6. 50-50")
            l5 = int(input())
            if l5 == 6:
                if fifty_fifty_used:
                    print("You have already used 50-50")
                    Display_List5()
                else:
                    fifty_fifty_used = True
                    del list6[1]
                    del list6[3]
                    for i in list6:
                        print(i)
                    l5 = int(input())
                    
            List6(l5)


name = input("What is your name? ")
clear_screen()
print(BLUE, "hey! " + name + " Welcome to our Gameshow")

print(RED, "-------------------------------------------")
print(RED, "-                                         -")
print(RED, "-                                         -")
print(YELLOW, "        KON BANEGA CRORE PATI           ")
print(RED, "-                                         -")
print(RED, "-                                         -")
print(RED, "-------------------------------------------")
pause()
time.sleep(0.5)
clear_screen()

print(YELLOW, "------RULES OF THE GAME------")
print(BLUE, "You have to answer 5 questions")
print(BLUE, "You have 4 options, and have to choose the right one")
print(RED, "1- You have the option of FLIP")
print(RED, "2- You can also use the option of 50-50")
print(BLUE, "For giving the correct answer, you will win 50$")
print(YELLOW, "Play game to win a total of 250$")
pause()
time.sleep(0.5)
clear_screen()

list1 = ["Which of the following is not a programming Language?", "1. Java","2. Cpp", "3. HTML","4. Python"]
list2 = ["Machine language is? ", "1. Similar to English abbreviation", "2. Made up of 1s and 0s", "3. Easy to modify", "4. Easy to read"]
list3=["Which of the following is low level language?","1. cpp","2. Java","3. Assembly","4. All of above"]
list4=["Which high level language is example of compiled language?","1. cpp","2. HTML","3. JavaScript","4. All of above"]
list5=["Void function has return type?","1. int","2. float","3. char","4. void"]
list6 = ["Computers think in the language of? ", "1. BASIC", "2. Binary", "3. FORTRAN ","4. COBOL"]

Display()
for i in list1:
    print(BLUE, i)
print("5.FLIP        6.50-50")
Display_List1()

pause()
time.sleep(0.5)
clear_screen()

Display()
for i in list2:
    print(BLUE, i)
print("5.FLIP        6.50-50")
Display_List2()

pause()
time.sleep(0.5)
clear_screen()

Display()
for i in list3:
    print(BLUE, i)
print("5.FLIP        6.50-50")
Display_List3()

pause()
time.sleep(0.5)
clear_screen()

Display()
for i in list4:
    print(BLUE, i)
print("5.FLIP        6.50-50")
Display_List4()

pause()
time.sleep(0.5)
clear_screen()

Display()
for i in list5:
    print(BLUE, i)
print("5.FLIP        6.50-50")
Display_List5()

pause()
time.sleep(0.5)
clear_screen()

Winning_Amount(*List)
