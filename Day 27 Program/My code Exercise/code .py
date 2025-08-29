
# Day = 27 
# date = 6-6-2025
# exercis 3 = create KBC type app
# use list datatype to store the question and their correct Answer
# display the final Amount the porsion is taking home After palying the game
# user input 
name_user = input ("Enter your name:")
print(f"Hi {name_user}\n Welcome to my KBC APP \n total Question my KBC app is 5")
print("1.Question right win 5000Rs\n2.Question right win 20000Rs\n3.Question right win 50000Rs\n4.Question right win 100000Rs\n5.Question right win 200000Rs")
ready = input("you are ready yes/no:")
# cerateing five list with Question
question_1 = ("1. what is the sum of to number 15+72\n>90\n>92\n>88\n>99")
question_2 = ("2.what is the multiplection of two number 5 X 15\n>74\n>84\n>75\n>62")
question_3 = ("3.what is creating python list symbol \n>()\n>/\n[]")
question_4 = ("4.x2 = 8,find the valeu of x \n>2\n>3\n>4\n>6")
question_5 = ("5.Total Question in KBC \n>15\n>5\n56")
#writing logic
if ready == "yes":
    print(question_1)
    Answer_1 = input("Enter your Answer:")
    if Answer_1 == "88":
        print("Answer is right")
        print(question_2)
        Answer_2 = input("Enter your Answer:")
        if Answer_2 =="75":
            print("answer is right")
            print(question_3)
            Answer_3 = input("Enter your Answer:")
            if Answer_3 =="[]":
                print("answer is right")
                print(question_4)
                Answer_4 = input("Enter your Answer:")
                if Answer_4 =="4":
                    print("answer is right")
                    print(question_5)
                    Answer_5 = input("Enter your Answer:")
                    if Answer_5 =="75":
                        print("answer is right")
                        print("very naice you win 200000Rs")
    if Answer_1 !="88":
        print("Answer is not right")
        print("you win bouns KBC App 500Rs")
    elif Answer_2 != "75":
        print("Answer is not right")
        print("you win 5000Rs")
    elif Answer_3 !="[]":
        print("Answer is not right")
        print("you win 20000Rs")
    elif Answer_4 != "4":
        print("Answer is not right")
        print("you win 50000Rs")
    elif Answer_5 !="5":
        print("Answer is not right ")
        print("you win 100000")
else:
    print("Thank you for using my App")