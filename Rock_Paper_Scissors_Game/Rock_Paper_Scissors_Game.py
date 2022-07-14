import random
print("\t\t\t\t\t**********************************************")
print("\t\t\t\t\t*******  Greeter - Hello new friends!  *******")
print("\t\t\t\t\t**********************************************")
print("\t\t\t\t\t************      1-Rock        **************")
print("\t\t\t\t\t************      2-Paper       **************")
print("\t\t\t\t\t************      3-Scissors    **************")
print("\t\t\t\t\t**********************************************")

user_score = 0
comp_score = 0
game_number = 0
while(game_number < 5):
    user_choice = int(input("Your choice: "))
    comp_choice = random.choice([1,2,3])

    if user_choice == 1:
        if comp_choice == 1:
            print("Computer choice is Rock and your choice is rock. Scorless!")
        elif comp_choice == 2:
            print("Computer choice is Paper and your choice is rock. Computer won!")
            comp_score +=100
        elif comp_choice == 3:
            print("Computer choice is Scissors and your choice is rock. You won!")
            user_score +=100
    elif user_choice == 2:
        if comp_choice == 1:
            print("Computer choice is Rock and your choice is rock. Scorless!")
        elif comp_choice == 2:
            print("Computer choice is Paper and your choice is rock. Computer won!")
            comp_score +=100
        elif comp_choice == 3:
            print("Computer choice is Scissors and your choice is rock. You won!")
            user_score +=100
    elif user_choice == 3:
        if comp_choice == 1:
            print("Computer choice is Rock and your choice is Scissors. Computer won!!")
            comp_score +=100
        elif comp_choice == 2:
            print("Computer choice is Paper and your choice is Scissors. Computer won!")
            user_score +=100
        elif comp_choice == 3:
            print("Computer choice is Scissors and your choice is Scissors. Scorless!")
    else:
        break
    game_number+=1

print("\nComputer Score: {}, User Score: {}".format(comp_score, user_score))
            
