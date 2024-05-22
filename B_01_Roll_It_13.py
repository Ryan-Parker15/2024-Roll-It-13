# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instruction():
    print('''
    
**** Instructions ****

To begin, decide the overall score needed to be crowned the winner of the game (eg: first person to get a score of 50 or more).
At the start of each round, the user and the computer each roll two dice.  The initial number of points for each player is the total shown by the dice.  Then, taking turns, the user and computer each roll a single die and add the result to their points.  The goal is to get 13 points (or slightly less) for a given round.  Once you are happy with your number of points, you can ‘pass’.
If you go over 13, then you lose the round (and get zero points). 
If the computer goes over 13, the round ends and your score is the number of points that you have earned.
If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays the same).  
If you get more points than the computer (but less than 14 points), you win and add your points to your score.  The computer’s score stays the same. 
If the first roll of your dice is a double, then your score is increased by double the number of points, provided you win.  If the computer’s first roll of the dice is a double, then its points are not doubled (this gives the human player a slight advantage).


The ultimate winner of the game is the first one to get to the specified score goal.

Good luck
    ''')


# checks that users enter an integer
# that is more than 13
def int_check():
    while True:

        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input("Enter an integer:  "))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine
print()
print("🎲🎲 Roll it 13🎲🎲")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print()
target_score = int_check()

