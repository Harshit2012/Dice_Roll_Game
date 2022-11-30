import random

min_val = 1
max_val = 53

roll_again = "Yes"

while roll_again == "Yes" or roll_again == "y":
    print("Rolling The Dices")
    print("The values are")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again = input("Roll Dices Again?")