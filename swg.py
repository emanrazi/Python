import random

print("1. To Select SNAKE")
print("2. To Select WATER")
print("3. To Select GUN")

choice = int(input("Enter your choice: "))
system = random.randint(1, 3)
print("Your system selects:", system)

if choice == system:
    print("Game is draw")
elif (choice == 1 and system == 2) or (choice == 2 and system == 3) or (choice == 3 and system == 1):
    print("You win the game")
elif (choice == 1 and system == 3) or (choice == 2 and system == 1) or (choice == 3 and system == 2):
    print("You lose!! and Your system wins")
else:
    print("Invalid input")
