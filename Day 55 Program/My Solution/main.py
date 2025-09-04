
#Day 55 100 days of code 
#Date 8/7/2025

#----------------------------------------------Exercise 5 Create Snake Water Gun Game in python -------------------------------------------------
#Uaers win case 
# computer = Snake and user = water
# computer = water and user = gun
# computer = gun and user = snake 

#--------------------------------------------------------------------------

#computer win case
# computer = water and user = snake
# computer = gun and user = water
# computer = snake and user = gun

#--------------------------------------------------------------------------

#user lose case
# computer = snake and user = gun 
# computer = water and user = snake
# computer = gun and user = water

#--------------------------------------------------------------------------

# computer lose case
# computer = gun and user = snake
# computer = snake and user = water
# computer = water and user = gun

#--------------------------------------------------------------------------
# game drow case
# computer = snake and user = snake
# computer = water and user = water
# computer = gun and user = gun


#--------------------------------------------------------------------------
# MY CODE 

import random
while True:
    user = input(">> Snake for 0\n>> Water for 1\n>> Gun for 2\n>>Stop for quit\nEnter the choise : ")
    computer = random.choice(["1","0","2","0","1","2"])
    choise = {"0":"Snake","1":"Water","2":"Gun"}
    if computer == user:
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("Game is  Drow...")

    elif computer =="1" and user =="0":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("You win...")

    elif computer =="0" and user=="1":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("Computer win...")

    elif computer =="0" and user=="2":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("You win...")

    elif computer =="2" and user=="0":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("Computer win...")

    elif computer =="1" and user=="2":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("Computer win...")
    
    elif computer =="2" and user=="1":
        print(f"User Choise : {choise[user]} ")
        print(f"Computer choise :{choise[computer]}")
        print("You win...")

    elif user == "quit":
        print("Thank you for playing")
        break
        
    else:
        print("Invalid input please try again")

# finshed
#-------------------------------------------------------------------------- 