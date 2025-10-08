import random

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print(f"You rolled {die1} + {die2} = {total}")
    return total

def play_craps():
    print("Welcome to the Craps game!")

    first_roll = roll_dice()
    if first_roll in [7, 11]:
        print("You win!")
        return
    elif first_roll in [2, 3, 12]:
        print("Craps! Casino wins.")
        return
    else:
        goal = first_roll
        print(f"Your goal is to roll {goal} again before rolling a 7.")

    while True:
            roll = roll_dice()
            if roll == goal:
                print("You rolled your goal! You win!")
                break
            elif roll == 7:
                print("You rolled a 7 before your goal. You lose!")
                break
            else:
                print("Rolling again...")

play_craps()
