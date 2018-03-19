"""
write a recursive function diceRoll that accepts an integer representing a number of
6-sided dice to roll, and output all possible combinations of values that could
appear on the dice.

https://www.youtube.com/watch?v=Cl9U027Rb9s&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk&index=15
"""


def dice_roll(num_dices):
    chosen = []
    _dice_roll(num_dices, chosen)


def _dice_roll(num_dices, chosen):
    if num_dices == 0:
        # Base case
        print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in range(1, 7):
            # Choose
            chosen.append(i)
            # Explore
            _dice_roll(num_dices-1, chosen)
            # BackTrack
            chosen.pop()


def generic_dice_roll(num_decisions, options, chosen):
    if num_decisions == 0:
        # Base case
        print(chosen)
    else:
        # Some dices are left to role
        # Handle one dice
        # For each value that dice could have
        for i in options:
            # Choose
            chosen.append(i)
            # Explore
            generic_dice_roll(num_decisions-1, options, chosen)
            # BackTrack
            chosen.pop()


if __name__ == "__main__":
    print(dice_roll(2))
    print("**************")
    print(generic_dice_roll(3, ['a', 'b', 'c'], []))
